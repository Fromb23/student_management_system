#!/usr/bin/python3

import csv
from menu import print_menu

def view_profile(userName):
    with open('userInfo.csv', 'r', newline='') as csvfile:
        _profile = csv.DictReader(csvfile)

        for row in _profile:
            if row['username'] == userName:
                for key, value in row.items():
                    print(f"{key}: {value}")
    main_menu = input("To return to main menu, press 'y': ")
    if main_menu == 'y':
        print_menu()
