# this is the implementation of our FIT5163 DH Keyexchange
import random
import secrets


# key exchange process implementation
def key_exchange_process():
    # Implement two const for computation
    P = generate_large_prime()
    G = generate_base(P)

    # Simulate key exchange process
    # To do : need to implemetation Person object class
    alice = Person("Alice")
    bob = Person("Bob")







# main function
if __name__ == "__main__":
    # key exchange
    key_exchange_process()

    # simulate attack 

    # Add PAKE/OPAQUE protocol 
