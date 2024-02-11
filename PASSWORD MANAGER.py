python
from cryptography.fernet import Fernet

# Generate a key for encryption and decryption
key = Fernet.generate_key()
fernet = Fernet(key)

# Encrypt a password
password = "secretpassword".encode()
encrypted_password = fernet.encrypt(password)

# Decrypt the password
decrypted_password = fernet.decrypt(encrypted_password).decode()
#By following these steps, WE can create a secure password management system in Python using the cryptography library