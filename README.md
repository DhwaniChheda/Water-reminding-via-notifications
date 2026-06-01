# Water Reminder Notification System

A simple Python-based desktop reminder that sends silent notifications to help users stay hydrated during working hours. The application runs in the background and displays a water reminder every 40 minutes between 8:00 AM and 5:00 PM that reminds you to drink water while you work. Stay Hydrated!

## Setup

1. Install the required package:

   ```bash
   pip install pync
   ```

2. Run the application:

   ```bash
   nohup python water_reminder.py &
   ```

## Stop the Application

To stop the reminder service:

```bash
pkill -f water_reminder.py
```

## Change Reminder Time

Open `water_reminder.py` and modify:

```python
time.sleep(40 * 60)
```

Replace `40` with the desired interval in minutes.

## Change Working Hours

Modify the following variables:

```python
START_HOUR = 8
END_HOUR = 17
```

The application uses the system's local time and automatically pauses outside the configured working hours.
