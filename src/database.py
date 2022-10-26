from cgitb import text
from math import remainder
from sys import prefix
from src.reminder import PoliteReminder
import csv

def list_reminders():
    f = open("reminders.csv", "r")

    with f:
        reader = csv.reader(f)

        for row in reader:
            print()
            for e in row:
                print(e.ljust(32), end=' ')
        print()

def add_reminder(text):
    print()
    
    reminder = PoliteReminder(text)
    
    with open('reminders.csv', 'a+', newline='\n') as file:
        writer = csv.writer(file)
        writer.writerow([reminder.text])
