# My first cyber project && first py project
# simple password checker

print("Hi! I am password checker.")
print("Enter your password and let's see how secure it is.")
password = input("Enter your password: ")

def check_password(password,element):
    for char in password:
        if char == element:
            return True
    return False
def contains_number(password):
    for char in password:
        if char.isdigit():
            return True
    return False

def contains_uppercase(password):
    for char in password:
        if char.isupper():
            return True
    return False

def contains_lowercase(password):
    for char in password:
        if char.islower():
            return True
    return False

def contains_special(password):
    specials = "!@#$%^&*?"
    for char in password:
        if char in specials:
            return True
    return False
conditions = [
contains_number(password),
contains_uppercase(password),
contains_lowercase(password),
contains_special(password),
(len(password) > 8)
]
score = sum(conditions)
print("score of your password out of 5 is: ", score)
if not contains_number(password):
    print("Your password does not contain a number.")
if not contains_uppercase(password):
    print("Your password does not contain a uppercase.")
if not contains_lowercase(password):
    print("Your password does not contain a lowercase.")
if not contains_special(password):
    print("Your password does not contain a special character.")
if not len(password) > 8:
    print("Your password is too short.")
