#!/usr/bin/python3

import csv

def user_details(userName):
    with open('userInfo.csv', 'r', newline='') as csvfile:
        user_info = csv.DictReader(csvfile)

        for row in user_info:
            if row['username'] == userName:
                userName, userStatus, usertype = row['username'], row['status'], row['usertype']
                return userName, userStatus, usertype
