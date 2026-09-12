# main.py

from scheduler import start_scheduler
from report import show_report

from medicine_schedule import (
    add_medicine,
    view_medicines,
    edit_medicine,
    delete_medicine
)


def main():

    while True:

        print("\n===================================")
        print(" SMART MEDICINE WATER BOTTLE")
        print("===================================")
        print("1. Start Reminder")
        print("2. View Daily Report")
        print("3. Add Medicine")
        print("4. View Medicines")
        print("5. Edit Medicine")
        print("6. Delete Medicine")
        print("7. Exit")

        choice = input("Enter Choice : ")

        if choice == "1":
            start_scheduler()

        elif choice == "2":
            show_report()

        elif choice == "3":
            add_medicine()

        elif choice == "4":
            view_medicines()

        elif choice == "5":
            edit_medicine()

        elif choice == "6":
            delete_medicine()

        elif choice == "7":
            print("\n===================================")
            print(" Thank You for Using")
            print(" SMART MEDICINE WATER BOTTLE")
            print("===================================")
            break

        else:
            print("\n❌ Invalid Choice! Please try again.")


if __name__ == "__main__":
    main()