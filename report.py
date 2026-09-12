# report.py

import csv
import os

FILE_NAME = "database.csv"


def show_report():
    if not os.path.exists(FILE_NAME):
        print("\nNo records found.")
        return

    water_total = 0
    medicine_taken = 0
    medicine_missed = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:

            if row["Event"] == "Water":
                try:
                    amount = int(row["Status"].replace(" ml", ""))
                    water_total += amount
                except:
                    pass

            elif row["Event"] == "Medicine":

                if row["Status"] == "Taken":
                    medicine_taken += 1

                elif row["Status"] == "Missed":
                    medicine_missed += 1

    print("\n==============================")
    print(" SMART MEDICINE BOTTLE REPORT ")
    print("==============================")
    print(f"💧 Total Water Intake : {water_total} ml")
    print(f"💊 Medicine Taken     : {medicine_taken}")
    print(f"❌ Medicine Missed    : {medicine_missed}")
    print("==============================")