# scheduler.py

import schedule
import time

from reminder import drink_water, take_medicine
from config import WATER_TIME
from medicine_schedule import get_medicines


# ----------------------------
# Water Reminder
# ----------------------------
def schedule_water():
    schedule.every().day.at(WATER_TIME).do(drink_water)


# ----------------------------
# Medicine Reminder
# ----------------------------
def schedule_medicines():

    medicines = get_medicines()

    if len(medicines) == 0:
        print("⚠ No medicines available.")
        return

    for medicine in medicines:

        schedule.every().day.at(medicine["Time"]).do(
            take_medicine,
            medicine["Medicine"],
            medicine["Dosage"],
            medicine["BeforeAfterFood"],
            medicine["Frequency"]
        )

        print(f"✅ Scheduled : {medicine['Medicine']} at {medicine['Time']}")


# ----------------------------
# Start Scheduler
# ----------------------------
def start_scheduler():

    schedule.clear()

    schedule_water()

    schedule_medicines()

    print("\n========================================")
    print(" SMART MEDICINE WATER BOTTLE")
    print("========================================")
    print("Reminder System Running...")
    print("Press Ctrl + C to Stop")
    print("========================================")

    while True:
        schedule.run_pending()
        time.sleep(1)