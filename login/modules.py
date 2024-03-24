#!/usr/bin/python3

import csv
import os

def modules(usertype):
    print(usertype)

    if usertype == 'Student':
        with open('modules.csv', 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                for key, value in row.items():
                    print(f"{key}: {value}")
    else:
        print("You are about to register a new Module into the system")
        field_names = ['unit code', 'course name']
        unit_code = input("Please enter the course code: ")
        unit_name = input("Please enter the course name: ")

        course_data = [{'unit code': unit_code, 'course name': unit_name}]

        course_exist = False

        writer = None
        if not os.path.exists('modules.csv') or os.stat('modules.csv').st_size == 0:
            # Create the file or write to it if it's empty
            with open('modules.csv', 'a', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=field_names)
                writer.writeheader()
        else:
            # Open the file if it exists and is not empty
            with open('modules.csv', 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)

                for row in reader:
                    if row['unit code'] == unit_code:
                        print("A similar unit code already exist")
                        return

        # Write data to the file
        with open('modules.csv', 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=field_names)
            writer.writerows(course_data)
            print("You have successfully registered a new module")
