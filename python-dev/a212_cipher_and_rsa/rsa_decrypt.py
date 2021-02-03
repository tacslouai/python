#   a212_rsa_decrypt.py
import rsa as rsa
sender=input("who sent you this message?")
print("If they sent you the message, then",sender,"should have used your public key to encrypt")
key = int(input("Enter your Private Key: " ))
mod_value = int(input("Enter your Modulus: " ))
encrypted_msg = input("Paste in the message they sent you with no brackets and hit enter: ")

#break apart the list that is cut/copied over on ", "
msg = encrypted_msg.split(", ")
print (rsa.decrypt(key,mod_value , msg))
