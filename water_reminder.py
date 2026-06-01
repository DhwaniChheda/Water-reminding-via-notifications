from pync import Notifier
from datetime import datetime
import time

START_HOUR = 8
END_HOUR = 17

while True:
    now = datetime.now()
    current_hour = now.hour
    if START_HOUR <= current_hour < END_HOUR:
        Notifier.notify(
            "Drink some water 💧",
            title="Water Reminder"
        )
        time.sleep(2400)

    else: time.sleep(3600)