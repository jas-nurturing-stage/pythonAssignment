# pythonAssignment
Question1 : Check_Password_Strength
Explaining each code of line:
_import re : "re module", which stands for regular expressions, Regex are used for pattern matching in strings.
I have used it to check whether the password contains specific character types (uppercase, lowercase, digits, special characters).
_def check_password_strength(password): function named check_password_strength, which takes one argument: password.
The purpose of this function is to evaluate strength of a given password.
if len(password) < 8:
    return "Password should be at least 8 characters long." # Checking password length.
Above condition is True, the function immediately returns a message. Using return stops the function from running further.
if not re.search(r'[A-Z]', password):  
    return "Password should contain at least one uppercase letter." # re.search(r'[A-Z]', password) looks for any uppercase letter (A to Z) inside the password.
then returns the message.
if not re.search(r'[a-z]', password):
    return "Password should contain at least one lowercase letter." # ensures that at least one lowercase letter (a to z) present in password. If no lowercase letter is found "returns".
if not re.search(r'\d', password): 
    return "Password should contain at least one digit." # \d is a special regex pattern that matches any digit (0-9). else returns message 
if not re.search(r'[\W_]', password):
    return "Password should contain at least one special character." # \W is a regex pattern that matches any non-alphanumeric character (anything that is not A-Z, a-z, or 0-9).
_ (underscore) is explicitly included because it's sometimes considered a special character.
return "Password is strong." # If the password passes all previous checks, then meets all strength requirements.
password = input("Enter a password: ")
result = check_password_strength(password) # This calls the function check_password_strength() with the user-entered password.
print(result)
![image](https://github.com/user-attachments/assets/ae85a671-80f1-41fd-bb5c-4d258bedb2e6)


