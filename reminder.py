# reminder.py

from plyer import notification
import winsound
from logger import save_log


# -----------------------------------
# Alarm Sound
# -----------------------------------
def play_alarm():

    winsound.Beep(1000, 1000)


# -----------------------------------
# Desktop Notification
# -----------------------------------
def show_notification(title, message):

    notification.notify(
        title=title,
        message=message,
        timeout=10
    )


# -----------------------------------
# Water Reminder
# -----------------------------------
def drink_water():

    play_alarm()

    show_notification(
        "💧 Water Reminder",
        "Time to drink water!"
    )

    print("\n================================")
    print("       WATER REMINDER")
    print("================================")

    while True:

        try:

            amount = int(
                input("Enter water consumed (ml): ")
            )

            save_log(
                "Water",
                f"{amount} ml"
            )

            print(
                f"\n✅ Water intake saved : {amount} ml"
            )

            break

        except ValueError:

            print(
                "❌ Please enter a valid number."
            )


# -----------------------------------
# Medicine Reminder
# -----------------------------------
def take_medicine(
    name,
    dosage,
    food,
    frequency
):

    play_alarm()

    show_notification(
        "💊 Medicine Reminder",
        f"{name}\n{dosage}"
    )

    print("\n========================================")
    print("       SMART MEDICINE REMINDER")
    print("========================================")

    print(f"Medicine  : {name}")
    print(f"Dosage    : {dosage}")
    print(f"Food      : {food}")
    print(f"Frequency : {frequency}")

    print("========================================")
    print("1. Medicine Taken")
    print("2. Snooze (5 Minutes)")
    print("3. Skip")
    print("========================================")

    choice = input("Enter Choice : ")

    # -----------------------------------
    # Medicine Taken
    # -----------------------------------
    if choice == "1":

        print("\n✅ Medicine Taken")

        save_log(
            "Medicine",
            f"{name} - Taken"
        )

    # -----------------------------------
    # Snooze
    # -----------------------------------
    elif choice == "2":

        print("\n⏰ Medicine Snoozed")

        save_log(
            "Medicine",
            f"{name} - Snoozed"
        )

    # -----------------------------------
    # Medicine Skipped
    # -----------------------------------
    elif choice == "3":

        print("\n❌ Medicine Skipped")

        save_log(
            "Medicine",
            f"{name} - Skipped"
        )

    else:

        print("\n⚠ Invalid Choice")