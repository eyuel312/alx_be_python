from datetime import datetime, timedelta
def display_current_datetime():
    current_date = datetime.now()
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted)
    return current_date  
def calculate_future_date(current_date):
    days = int(input("Enter the number of days to add to the current date: "))
    future_date = current_date + timedelta(days=days)
    print("Future date:", future_date.strftime("%Y-%m-%d")) 
def main():
    current_date = display_current_datetime()
    calculate_future_date(current_date)
if name == "__main__":
    main()
