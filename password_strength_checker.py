import re

def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."
    elif not re.search("[a-z]", password) or not re.search("[A-Z]", password):
        return "Moderate: Password should include both uppercase and lowercase letters."
    elif not re.search("[0-9]", password):
        return "Moderate: Password should contain numbers."
    elif not re.search("[@#$]", password):
        return "Strong but could be better with special characters (@, #, $)."
    else:
        return "Very Strong!"

password = input("Enter a password to check its strength: ")
print(check_password_strength(password))
