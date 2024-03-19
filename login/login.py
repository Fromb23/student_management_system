#!/usr/bin/python3

import getpass
import sys
import csv
from user_details import user_details

def login():
    print("Welcome to Module and Student system")
    attempts = 0
    status = []
    max_attempts = 3
    if sys.stdin.isatty():
        userName = input("Enter user name: ")
        print(userName)
        user_exists = False
    with open('userInfo.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            if row['username'] == userName:
                user_exists = True
            if not user_exists:
                print("User name not found")
                break

    if user_exists:
        #enter passwd
        while attempts < max_attempts:
            right_password = False
            passwd = getpass.getpass("password for " + userName + ":")
            with open('userInfo.csv', 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if row['password'] == passwd and row['username'] == userName:
                        print("usr_exist")
                        print("password match")
                        userName, status = user_details(userName)
                        print('You are logged in as '+ " "+ userName + ", " + "Account status is " + status + "...")
                        right_password = True
                        break;
                if right_password:
                    break
                else:
                    print("incorrect passwrd, please try again")
            attempts += 1

        if attempts == max_attempts:
            print("Access Denied, You've been Blocked!!!, please Contact the Admin for more")

if __name__ == '__main__':
    login()
