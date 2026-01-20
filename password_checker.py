import re

def check_password_strength(password):
    if len(password) < 8:
        return "Weak password"

    if not re.search("[A-Z]", password):
        return "Weak password"

    if not re.search("[a-z]", password):
        return "Weak password"

    if not re.search("[0-9]", password):
        return "Weak password"

    if not re.search("[@#$%&!]", password):
        return "Weak password"

    return "Strong password"

password = input("Enter password: ")
print(check_password_strength(password))
