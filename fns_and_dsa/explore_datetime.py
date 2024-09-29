#date time test

from datetime import datetime

from datetime import date

from datetime import timedelta

def display_current_datetime():

    current_date = datetime.now()
    
    time = current_date.strftime("%Y-%m-%d %H:%M:%S")

    print("Current date and time is ",time)

display_current_datetime()

def calculate_future_date():

    current_date = datetime.now()

    days_no = int(input("Enter the number of days to add to the current date: "))
               
    delta = timedelta(days = days_no)

    future_date = current_date + delta

    print(future_date.strftime("%Y-%m-%d %H:%M:%S"))

calculate_future_date()