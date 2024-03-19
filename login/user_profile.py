#!/usr/bin/python3

import csv

def user_profile():
    field_names = ['username', 'modules', 'password', 'usertype', 'status']
    data = [{'username': 'Fromb', 'modules': 'computer Science', 'password': 'Fromb@2024', 'usertype': 'Student', 'status': 'Active'},
            {'username': 'Wamae', 'modules': 'Software Engineering', 'password': 'Wamae2024', 'usertype': 'Lecturer', 'status': 'Active'}
            ] 
    with open('userInfo.csv', 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)

        writer.writeheader()

        for row in data:
            print(row)
            writer.writerow(row)

user_profile()
