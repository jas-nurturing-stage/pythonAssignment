import re       

def check_password_strength(password):
    # Check length
    if len(password) < 8:
        return "Password should be at least 8 characters long."

    # Check uppercase letters
    if not re.search(r'[A-Z]', password):    #re.search() searches for that particular pattern within the string.
        return "Password should contain at least one uppercase letter."

    # Check lowercase letters
    if not re.search(r'[a-z]', password):
        return "Password should contain at least one lowercase letter."

    # Check digits
    if not re.search(r'\d', password): #(1,2,....0)
        return "Password should contain at least one digit."

    # Check special characters
    if not re.search(r'[\W_]', password):#(!@#$%^&*_)
        return "Password should contain at least one special character."

    return "Password is strong."

password = input("Enter a password: ")
result = check_password_strength(password)
print(result) 