#!/usr/bin/python3

import csv
from os import path

def add_user():
    print("Hello welcomem you are about to register new user")

    field_names = ["username", "password", "usertype", "status"]

    username = input("Enter the new user name: ")
    password = input("Add password for the new user: ")
    usertype = input("Specify if the user is a student or Lecturer: ")
    status = input("new user is always Active: ")

    user_data = [{'username': username, 'password': password, 'usertype': usertype, 'status': status}]

    file_exist = False

    print(path.exists('userInfo.csv'))
    #check wether path exists
    #if true 
    #check wether the username already exist if not 
    #append the file
    #else create the file
    try:
        with open('userInfo.csv', 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                print("Hello")
                if row['username'] == username:
                    file_exist = True
                    print("A similar user already exist")
                    return
    except:
            try:
                with open('userInfo.csv', 'a', newline='') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=field_names)
                    writer.writeheader()

                    writer.writerows(user_data)
                    print("You've successfully registered a new user")

            except FileNotFoundError:
                print("File you are trying to open is unavailabe")
                return

add_user()
