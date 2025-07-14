import csv
import os
from datetime import datetime

def log_learning():
    topic = input("Topic: ")
    duration = float(input("Duration (in hours): "))
    notes = input("Notes (optional): ")
    rating = int(input("How would you rate this session? (1-5): "))
    date = datetime.now().strftime("%Y-%m-%d")

    file_exists = os.path.isfile("learning_log.csv")

    file = open("learning_log.csv", "a", newline="")
    writer = csv.writer(file)

    # ✅ Write headers if file doesn't exist
    if not file_exists:
        writer.writerow(["Topic","Duration","Notes","Rating","Date"])

    # ✅ Match the order above
    writer.writerow([topic,duration,notes,rating,date])

    file.close()
    print("✅ Entry saved!")

log_learning()
