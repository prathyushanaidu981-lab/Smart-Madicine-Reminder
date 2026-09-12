# 💊💧 Smart Medicine Water Bottle

A Python-based Smart Medicine Water Bottle system that provides medicine and water reminders, stores medicine schedules, tracks medicine intake, and generates daily reports.

The project is designed as a software prototype that can later be integrated with hardware such as ESP32, a buzzer, OLED display, push buttons, and water-level sensors.

---

## 📌 Project Overview

Taking medicines on time is important, but people may forget their scheduled doses. Drinking enough water throughout the day is also important.

The **Smart Medicine Water Bottle** helps users by providing:

- 💊 Medicine reminders
- 💧 Water-drinking reminders
- 🔔 Buzzer alerts
- 🖥️ Desktop notifications
- 📝 Medicine schedule management
- ✏️ Edit medicine details
- 🗑️ Delete medicines
- 📊 Daily medicine and water reports
- 💾 CSV-based data storage

The current version is implemented using **Python** and can later be connected to physical hardware.

---

# 🎯 Objectives

The main objectives of this project are:

1. Remind users to take medicines at the scheduled time.
2. Remind users to drink water.
3. Store medicine information permanently.
4. Allow users to add, view, edit, and delete medicines.
5. Track whether medicines were taken or skipped.
6. Generate daily reports.
7. Provide a foundation for future IoT hardware integration.

---

# ✨ Features

## 💊 Medicine Management

Users can:

- Add medicines
- View medicines
- Edit medicines
- Delete medicines

Each medicine contains:

| Field | Description |
|---|---|
| Medicine | Name of medicine |
| Dosage | Amount to take |
| Time | Reminder time |
| BeforeAfterFood | Before or after food |
| Frequency | Daily/Weekly |

Example:

```text
Medicine  : Paracetamol
Dosage    : 1 Tablet
Time      : 08:00
Food      : After Food
Frequency : Daily


