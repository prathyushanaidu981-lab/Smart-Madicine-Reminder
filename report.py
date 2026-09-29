import csv
import os

FILE_NAME = "database.csv"


def show_report():

    print("\n==============================")
    print(" SMART MEDICINE BOTTLE REPORT")
    print("==============================")

    if not os.path.exists(FILE_NAME):
        print("💧 Total Water Intake : 0 ml")
        print("💊 Medicine Taken     : 0")
        print("❌ Medicine Missed    : 0")
        print("==============================")
        return

    total_water = 0
    medicine_taken = 0
    medicine_missed = 0

    with open(FILE_NAME, "r", newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:

            event = row["Event"].strip()
            status = row["Status"].strip()

            # Water
            if event.lower() == "water":

                try:
                    amount = int(
                        status.lower()
                        .replace("ml", "")
                        .strip()
                    )

                    total_water += amount

                except ValueError:
                    pass

            # Medicine
            elif event.lower() == "medicine":

                status_lower = status.lower()

                if status_lower.endswith(" - taken"):
                    medicine_taken += 1

                elif status_lower.endswith(" - skipped"):
                    medicine_missed += 1

    print(f"💧 Total Water Intake : {total_water} ml")
    print(f"💊 Medicine Taken     : {medicine_taken}")
    print(f"❌ Medicine Missed    : {medicine_missed}")

    print("==============================")