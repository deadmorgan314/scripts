import os
import base64
from cryptography.fernet import Fernet

def encrypt(file):
      key = base64.urlsafe_b64encode(os.urandom(32))
      cip=Fernet(key)
      with open(file, "rb") as f:
         data = f.read()
      cip_text = cip.encrypt(data)
      with open(file, "wb") as f:
         f.write(cip_text)
      f.close()

file = input()
encrypt(file)


