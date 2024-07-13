from datetime import datetime, timedelta, date

def display_current_datetime() :

    current_date = datetime.now()
    return current_date



current_date = display_current_datetime()
print(current_date)

def calculate_future_date(number_of_days) : 
    
    future_date = date.today() + timedelta(days=number_of_days)
    
    return future_date

number_of_days = int(input("Enter the number of days to add to the current date:"))

future_date = calculate_future_date(number_of_days)

print(future_date)

