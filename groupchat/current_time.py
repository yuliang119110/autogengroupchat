# filename: current_time.py

from datetime import datetime

# Print the current system date and time
now = datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")
print("Current Date and Time:", current_time)