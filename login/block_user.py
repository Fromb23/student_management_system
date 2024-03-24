#!/usr/bin/python3

import csv

def block_user(userName):
    with open('userInfo.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        fieldnames = reader.fieldnames

        new_list = []
        for row in reader:
            print(type(row))
            if row['username'] == userName:
                row['status'] = 'Blocked'
            new_list.append(row)

    with open('userInfo.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(new_list)
