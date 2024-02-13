# DATE

# 1. Write a Python program to subtract five days from current date.

from datetime import datetime, timedelta
current_date = datetime.now() #current date
new_date = current_date - timedelta(days=5) # Subtract five days
print("Current date:", current_date.strftime("%Y-%m-%d"))    #year 4 digits, month and day in 2 digits
print("Date five days ago:", new_date.strftime("%Y-%m-%d"))  #strftime converts datetime to string


