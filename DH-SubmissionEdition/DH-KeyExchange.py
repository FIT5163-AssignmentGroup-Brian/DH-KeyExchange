# this is the implementation of our FIT5163 DH Keyexchange
import random
import secrets
from sympy import isprime
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15

# Define a class representing a participant, e.g., Theo or Knew
class Person:
    def __init__(self, name):
        self.name = name  
        self.P = None     
        self.G = None     
        self.private_key = None  
        self.public_key = None   
        self.shared_secret = None  
        self.signature_key = RSA.generate(2048)  

    def set_parameters(self, p, g):
        # Set the common parameters p and g
        self.P = p
        self.G = g

    def generate_keys(self):
        # Generate private and public keys
        self.private_key = secrets.randbelow(self.p - 2) + 2  # Random private key in range [2, p-1]
        self.public_key = pow(self.g, self.private_key, self.p)  

    def sign_data(self, data):
        # Sign data using RSA private key
        hasher = SHA256.new(data)  # Hash the data using SHA256
        signature = pkcs1_15.new(self.signature_key).sign(hasher)  # Generate signature
        return signature

    def verify_signature(self, data, signature, public_key):
        # Verify the signature using the counterpart's public key
        hasher = SHA256.new(data)
        try:
            pkcs1_15.new(public_key).verify(hasher, signature)
            return True  
        except (ValueError, TypeError):
            return False  

    def generate_shared_secret(self, other_public_key):
        # Compute the shared secret key
        self.shared_secret = pow(other_public_key, self.private_key, self.p)
        return self.shared_secret

    def __str__(self):
        # Return a string representation including name, public key, and shared secret
        return f"{self.name} - Public Key: {self.public_key}, Shared Secret: {self.shared_secret}"


# generate large Prime number
def generate_large_prime():
    while True:
        num = random.getrandbits(1024) # random number 1024bits
        if isprime(num):
            return num 


# generate base const based on Prime
def generate_base(num):
    return secrets.randbelow(num-2) + 2 # range [2,p-2]


# key exchange process implementation
def key_exchange_process(person1=Person("Theo") , person2=Person("Knew")):
    # Implement two const for computation
    P = generate_large_prime()
    G = generate_base(P)

    # Simulate key exchange process
    # To do : need to implemetation Person object class
    theo = person1
    knew = person2

    #compute constant
    theo.set_parameters(P,G)
    knew.set_parameters(P,G)

    #generate public and private keys
    theo.generate_keys()
    knew.generate_keys()

    #now we sign keys
    theo_PK_signed = theo.sign_data(str(theo.public_key).encode())
    knew_PK_signed = knew.sign_data(str(knew.public_key).encode())

    # exchange and verify
    if not theo.verify_signature(str(knew.public_key).encode(), knew_PK_signed, knew.signature_key.publickey()):
        print("Knew's key verfication failed")
        print("Key exchange process ended")
        return
    
    if not knew.verify_signature(str(theo.public_key).encode(), theo_PK_signed, theo.signature_key.publickey()):
        print("Theo's key verfication failed")
        print("Key exchange process ended")
        return

    # generate shared secret 
    theo_secret = theo.generate_shared_secret(knew.public_key)
    knew_secret = knew.generate_shared_secret(theo.public_key)

    # print(theo)
    # print(knew)
    assert theo_secret == knew_secret, "The shared secrets do not match!"
    print("Shared secret successfully established.")

def simulate_mitm_attack():
    # Simulate a man-in-the-middle attack

    # Generate common parameters p and g
    p = generate_large_prime()
    g = generate_base(p)

    # Create participants Theo, Knew, and attacker Eve
    theo = Person("Theo")
    knew = Person("Knew")
    eve = Person("Eve")  # The adversary 

    # Set common parameters and generate keys
    for person in [theo, knew, eve]:
        person.set_parameters(p, g)
        person.generate_keys()

    # sign their public keys
    theo_public_key_signed = theo.sign_data(str(theo.public_key).encode())
    knew_public_key_signed = knew.sign_data(str(knew.public_key).encode())

    # Eve intercepts and modifies the key exchange
    # Eve sends her own public key to Knew instead of Theo's
    if not knew.verify_signature(str(eve.public_key).encode(), theo_public_key_signed, theo.signature_key.publickey()):
        print("Man-in-the-middle detected: Theo's key verification failed")
        return  # Stop exchange on detection

    # Theo verifies Knew's public key normally
    if not theo.verify_signature(str(knew.public_key).encode(), knew_public_key_signed, knew.signature_key.publickey()):
        print("Man-in-the-middle detected: Knew's key verification failed")
        return

    # Step 6: Generate shared secrets with wrong keys
    theo_secret = theo.generate_shared_secret(knew.public_key)
    knew_secret = knew.generate_shared_secret(eve.public_key)  # Knew uses Eve's key instead of Theo's

    # Step 7: Print results
    # print(theo)
    # print(knew)

    # Step 8: Validate that shared secrets match (they will not)
    assert theo_secret == knew_secret, "The shared secrets do not match!"

    print("Man-in-the-middle attack did not disrupt the key exchange.")










# main function
if __name__ == "__main__":

    theo = Person("Theo")
    knew = Person("Knew")
    # key exchange
    key_exchange_process(theo,knew)

    # simulate attack 

    # Add PAKE/OPAQUE protocol 
