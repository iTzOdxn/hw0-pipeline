import base64
import datetime

print("=== DevSecOps Security App ===")
username = "iTzOdxn"

# Κρυπτογράφηση του ονόματος σε Base64
encoded_name = base64.b64encode(username.encode('utf-8')).decode('utf-8')

print(f"Timestamp: {datetime.datetime.now()}")
print(f"Original User: {username}")
print(f"Encrypted ID: {encoded_name}")
print("==============================")
