#!/usr/bin/python3

import csv

def view_profile(userName):
    with open('userInfo.csv', 'r', newline='') as csvfile:
        _profile = csv.DictReader(csvfile)

        for row in _profile:
            if row['username'] == userName:
                profile_list = list(row.items())
                print(profile_list)
