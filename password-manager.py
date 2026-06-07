import hashlib #hashing master password
import json #saving data
import os #checking if file exists
from cryptography.fernet import Fernet


def create(config):
    print("enter password")
    password = input()
    hashed_password = hashlib.sha256 (password.encode()).hexdigest()
    config["master_password"] = hashed_password
    json.dump(config, open("config.json", "w"))
    return config
config = {}

#encryption key|binary data
if os.path.exists('vault.key'):
    key = open("vault.key","rb").read()
else:
    key = Fernet.generate_key()
    open("vault.key","wb").write(key)
fernet = Fernet(key)

#master password
if os.path.exists('config.json'):
    config = json.load(open('config.json'))
else:
    create(config)

def login (config):
    print("enter password")
    password = input()
    hashed_password = hashlib.sha256 (password.encode()).hexdigest()
    if config["master_password"] == hashed_password:
        return True
    else:
        return False
logged_in = login(config)
if logged_in:
    print("logged in")
    action = input("enter action : add/remove/see")
    if action == "add":
        print("enter account platform")
        platform = input()
        print("enter password")
        password = input()
        encrypted_password = fernet.encrypt(password.encode())
        config[platform] = encrypted_password.decode()
        json.dump(config, open("config.json", "w"))
    if action == "remove":
        print("enter account platform")
        platform = input()
        del config[platform]
        json.dump(config, open("config.json", "w"))
    if action == "see":
        print("enter account platform")
        platform = input()
        print(f"password: {fernet.decrypt(config[platform].encode()).decode()}")
else:
    print("not logged in")
