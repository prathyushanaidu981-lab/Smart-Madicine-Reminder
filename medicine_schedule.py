# medicine_schedule.py

import csv
import os

FILE_NAME = "medicines.csv"


# ----------------------------------------
# Create medicines.csv if it doesn't exist
# ----------------------------------------
def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                "Medicine",
                "Dosage",
                "Time",
                "BeforeAfterFood",
                "Frequency"
            ])


# ----------------------------------------
# Add Medicine
# ----------------------------------------
def add_medicine():

    create_file()

    print("\n====================================")
    print("         ADD MEDICINE")
    print("====================================")

    name = input("Medicine Name           : ")
    dosage = input("Dosage (1 Tablet etc.)  : ")
    reminder_time = input("Reminder Time (HH:MM)   : ")
    food = input("Before/After Food       : ")
    frequency = input("Frequency (Daily/Weekly): ")

    with open(FILE_NAME, "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            name,
            dosage,
            reminder_time,
            food,
            frequency
        ])

    print("\n✅ Medicine Added Successfully!")


# ----------------------------------------
# View Medicines
# ----------------------------------------
def view_medicines():

    create_file()

    with open(FILE_NAME, "r") as file:

        reader = csv.DictReader(file)
        medicines = list(reader)

    if len(medicines) == 0:
        print("\n⚠ No medicines available.")
        return

    print("\n========================================")
    print("          MEDICINE LIST")
    print("========================================")

    for i, row in enumerate(medicines, start=1):

        print(f"\nMedicine #{i}")
        print("----------------------------------------")
        print(f"Medicine  : {row['Medicine']}")
        print(f"Dosage    : {row['Dosage']}")
        print(f"Time      : {row['Time']}")
        print(f"Food      : {row['BeforeAfterFood']}")
        print(f"Frequency : {row['Frequency']}")


# ----------------------------------------
# Edit Medicine
# ----------------------------------------
def edit_medicine():

    create_file()

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        medicines = list(reader)

    if len(medicines) == 0:
        print("\n⚠ No medicines available.")
        return

    print("\n========== MEDICINE LIST ==========")

    for i, med in enumerate(medicines, start=1):
        print(f"{i}. {med['Medicine']} ({med['Time']})")

    try:
        choice = int(input("\nEnter medicine number to edit: "))

        if choice < 1 or choice > len(medicines):
            print("❌ Invalid choice.")
            return

    except ValueError:
        print("❌ Please enter a valid number.")
        return

    medicine = medicines[choice - 1]

    print("\nPress Enter to keep the current value.")

    new_name = input(f"Medicine Name [{medicine['Medicine']}]: ")
    new_dosage = input(f"Dosage [{medicine['Dosage']}]: ")
    new_time = input(f"Time [{medicine['Time']}]: ")
    new_food = input(f"Food [{medicine['BeforeAfterFood']}]: ")
    new_frequency = input(f"Frequency [{medicine['Frequency']}]: ")

    if new_name:
        medicine["Medicine"] = new_name

    if new_dosage:
        medicine["Dosage"] = new_dosage

    if new_time:
        medicine["Time"] = new_time

    if new_food:
        medicine["BeforeAfterFood"] = new_food

    if new_frequency:
        medicine["Frequency"] = new_frequency

    with open(FILE_NAME, "w", newline="") as file:

        fieldnames = [
            "Medicine",
            "Dosage",
            "Time",
            "BeforeAfterFood",
            "Frequency"
        ]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(medicines)

    print("\n✅ Medicine Updated Successfully!")


# ----------------------------------------
# Delete Medicine
# ----------------------------------------
def delete_medicine():

    create_file()

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        medicines = list(reader)

    if len(medicines) == 0:
        print("\n⚠ No medicines available.")
        return

    print("\n========== MEDICINE LIST ==========")

    for i, med in enumerate(medicines, start=1):
        print(f"{i}. {med['Medicine']} ({med['Time']})")

    try:
        choice = int(input("\nEnter medicine number to delete: "))

        if choice < 1 or choice > len(medicines):
            print("❌ Invalid choice.")
            return

    except ValueError:
        print("❌ Please enter a valid number.")
        return

    deleted = medicines.pop(choice - 1)

    with open(FILE_NAME, "w", newline="") as file:

        fieldnames = [
            "Medicine",
            "Dosage",
            "Time",
            "BeforeAfterFood",
            "Frequency"
        ]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(medicines)

    print(f"\n✅ '{deleted['Medicine']}' deleted successfully!")


# ----------------------------------------
# Return medicines to scheduler.py
# ----------------------------------------
def get_medicines():

    create_file()

    with open(FILE_NAME, "r") as file:

        reader = csv.DictReader(file)

        medicines = list(reader)

    return medicines