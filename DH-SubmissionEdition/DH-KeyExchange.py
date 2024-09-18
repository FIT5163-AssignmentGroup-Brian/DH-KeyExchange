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
def key_exchange_process():
    # Implement two const for computation
    P = generate_large_prime()
    G = generate_base(P)

    # Simulate key exchange process
    # To do : need to implemetation Person object class
    theo = Person("Theo")
    knew = Person("Knew")







# main function
if __name__ == "__main__":
    # key exchange
    key_exchange_process()

    # simulate attack 

    # Add PAKE/OPAQUE protocol 
