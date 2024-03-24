#!/usr/bin/python3

import getpass
import sys
import csv
from user_details import user_details
from menu import print_menu
from my_profile import view_profile
from modules import modules
from block_user import block_user


def login():
    print("Welcome to Module and Student system")
    attempts = 0
    status = []
    usertype = None
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
                        userName, status,usertype = user_details(userName)
                        print('You are logged in as '+ " "+ userName + ", " + "Account status is " + status + "...")
                        print()
                        print_menu()
                        select_option = int(input("Select menu from the above options or 4 to Exit...: "))
                        if select_option == 1:
                            view_profile(userName)
                        elif select_option == 2:
                            modules(usertype)
                        elif select_option == 4:
                            print("You've successfully opted out")
                            exit()
                                
                        right_password = True
                        break;
                if right_password:
                    break
                else:
                    print("incorrect passwrd, please try again")
            attempts += 1

        if attempts == max_attempts:
            block_user(userName)
            print("Access Denied, You've been Blocked!!!, please Contact the Admin for more")

if __name__ == '__main__':
    login()
