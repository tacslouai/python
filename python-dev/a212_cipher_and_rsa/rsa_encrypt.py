#   a212_rsa_encrypt.py
import rsa as rsa

reciever=input("who are you sending this message to?")
print("Make sure to use", reciever, "'s keys to encrypt your message")
key = int(input("Enter the intended person's public Key: " ))
mod_value = int(input("Enter the intended person's Modulus: " ))
plaintext = input("Enter a message to encrypt: ")
encrypted_msg = rsa.encrypt(key, mod_value, plaintext)
print("Encrypted Message:", encrypted_msg)
