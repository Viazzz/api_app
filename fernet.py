from cryptography.fernet import Fernet
key = Fernet.generate_key()
print(key.decode())

"ewmzMKBWFtuyrBvP2v3eZkJv5Z-nYjHQxaOjVS2t5JA="