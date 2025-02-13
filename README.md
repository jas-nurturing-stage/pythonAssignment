# pythonAssignment
. Question1 : Check_Password_Strength
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

#Question2 : Monitoring 
Explanation about how can we monitor the cpu usage, disk space usage etc, I have given 40 % alert, In real time scenario threhold will be given 80 %.
Python script monitors CPU usage using the psutil library and alerts when CPU usage exceeds a predefined threshold.
psutil: Provides system and process utilities, including CPU, memory, disk, and network usage.time: Allows the script to pause execution for controlled monitoring.
The CPU usage threshold is set to 40% (threshold = 40).The script continuously checks CPU usage and prints an alert when usage surpasses the threshold.
Monitoring CPU Usage (monitor_cpu_usage function): Runs an infinite loop to monitor CPU usage.Used psutil.cpu_percent(interval=1) to fetch CPU usage.
If CPU usage exceeds the threshold, it prints an alert.Used time.sleep(1) to avoid excessive CPU consumption by the script itself.
Handles interruptions (Ctrl+C) and other exceptions gracefully.
Examples : We can monitor server_Load_Monitoring, Monitoring Edge devices (IoT), Performance testing.
![image](https://github.com/user-attachments/assets/18ae1212-2b6c-4d37-b62f-216fc66cc1b8)

#Question3: Backup files 
This Python script automates file backups from a source folder to a destination folder. If a file with the same name already exists in the destination, the script adds a timestamp to prevent overwriting.
import os, shutil, datetime os: Handles file and directory operations,shutil: Copies files from one location to another,datetime: Generates timestamps to differentiate backups.
def backup_files_with_timestamp(source_folder, destination_folder):
for file_name in os.listdir(source_folder):                    # os.listdir(source_folder) gets a list of all files in the source directory
    source = os.path.join(source_folder, file_name)            # os.path.join(...) creates full file paths for copying
    destination = os.path.join(destination_folder, file_name)
if os.path.isfile(destination):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    new_destination = os.path.join(destination_folder, timestamp + " - " + file_name)
    shutil.copy(source, new_destination)
else:
    shutil.copy(source, destination)
if __name__ == "__main__":
    source_folder = r"C:\Users\jasmi\Desktop\Test file"               # Sets source and destination folder paths.
    destination_folder = r"C:\Users\jasmi\Desktop\Projects"           # Calls the backup function when executed directly.
    backup_files_with_timestamp(source_folder, destination_folder)
Real time scenarios : Preventing Data Loss in System Administration like .conf, .json, Before updating Nginx configuration (nginx.conf), it gets copied with a timestamp,  
                        Can be modified to upload backups to AWS S3, Google Drive, or Azure Blob Storage. Log File Archiving in DevOps Web server logs (access.log) can be backed up daily.
                        example : Backup: 2025-02-13-00-00-01 - access.log
![B4 backup of testfile](https://github.com/user-attachments/assets/ce3a8f88-0da1-4c5d-8ee7-48521ac115f2)
![B4 backup of project folder](https://github.com/user-attachments/assets/f1a59027-58d4-4916-a008-8966f8a13873)
![Backup of projects](https://github.com/user-attachments/assets/a40d6a28-4e9a-47d8-85e1-955b054cbdb1)


                     





