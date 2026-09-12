import csv
import os
from datetime import datetime

FILE_NAME = "database.csv"

def save_log(event, status):
    file_exists = os.path.isfile(FILE_NAME)

    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)

        # Write header only once
        if not file_exists:
            writer.writerow(["Date", "Time", "Event", "Status"])

        current_date = datetime.now().strftime("%d-%m-%Y")
        current_time = datetime.now().strftime("%H:%M:%S")

        writer.writerow([current_date, current_time, event, status])