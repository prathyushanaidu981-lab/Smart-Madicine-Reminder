# scheduler.py

import schedule
import time
from datetime import datetime

from reminder import drink_water, take_medicine
from config import WATER_TIMES
from medicine_schedule import get_medicines


# -----------------------------------
# Check Time Format
# -----------------------------------
def valid_time(time_value):

    try:
        datetime.strptime(time_value, "%H:%M")
        return True

    except ValueError:
        return False


# -----------------------------------
# Schedule Water Reminders
# -----------------------------------
def schedule_water():

    for water_time in WATER_TIMES:

        if valid_time(water_time):

            schedule.every().day.at(water_time).do(
                drink_water
            )

            print(
                f"💧 Water reminder scheduled at {water_time}"
            )

        else:

            print(
                f"❌ Invalid water time: {water_time}"
            )


# -----------------------------------
# Schedule Medicine Reminders
# -----------------------------------
def schedule_medicines():

    medicines = get_medicines()

    if not medicines:

        print("⚠ No medicines available.")

        return

    for medicine in medicines:

        name = medicine["Medicine"]
        dosage = medicine["Dosage"]
        medicine_time = medicine["Time"]
        food = medicine["BeforeAfterFood"]
        frequency = medicine["Frequency"]

        if not valid_time(medicine_time):

            print(
                f"❌ Invalid time for {name}: "
                f"{medicine_time}"
            )

            continue

        if frequency.lower() == "daily":

            schedule.every().day.at(
                medicine_time
            ).do(
                take_medicine,
                name,
                dosage,
                food,
                frequency
            )

            print(
                f"💊 Medicine scheduled: "
                f"{name} at {medicine_time}"
            )

        else:

            print(
                f"⚠ Frequency '{frequency}' "
                f"is not supported yet."
            )


# -----------------------------------
# Start Scheduler
# -----------------------------------
def start_scheduler():

    schedule.clear()

    print("\n===================================")
    print(" SMART MEDICINE WATER BOTTLE")
    print("===================================")

    schedule_water()

    schedule_medicines()

    print("\nReminder System Running...")
    print("Press Ctrl + C to stop.")
    print("===================================\n")

    try:

        while True:

            schedule.run_pending()

            time.sleep(1)

    except KeyboardInterrupt:

        print("\nReminder System Stopped.")