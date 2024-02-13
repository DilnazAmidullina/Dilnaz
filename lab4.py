# DATE

# 1. Write a Python program to subtract five days from current date.

# from datetime import datetime, timedelta
# current_date = datetime.now() #current date
# new_date = current_date - timedelta(days=5) # Subtract five days
# print("Current date:", current_date.strftime("%Y-%m-%d"))    #year 4 digits, month and day in 2 digits
# print("Date five days ago:", new_date.strftime("%Y-%m-%d"))  #strftime converts datetime to string


# 2. Write a Python program to print yesterday, today, tomorrow.

# from datetime import datetime, timedelta

# current_date = datetime.now()
# yesterday = current_date - timedelta(days=1)
# tomorrow = current_date + timedelta(days=1)

# print("Yesterday:", yesterday.strftime("%Y-%m-%d"))
# print("Today:", current_date.strftime("%Y-%m-%d"))
# print("Tomorrow:", tomorrow.strftime("%Y-%m-%d"))


# 3. Write a Python program to drop microseconds from datetime.

# from datetime import datetime
# current_datetime = datetime.now()
# without_microseconds = current_datetime.replace(microsecond=0)

# print("Datetime without microseconds:", without_microseconds)


# 4. Write a Python program to calculate two date difference in seconds

from datetime import datetime
date1 = datetime(2024, 2, 13, 12, 0, 0)  # Example date 1
date2 = datetime(2024, 2, 12, 12, 0, 0)  # Example date 2

difference_in_seconds = abs((date1 - date2).total_seconds())
print("Difference between the two dates in seconds:", difference_in_seconds)
