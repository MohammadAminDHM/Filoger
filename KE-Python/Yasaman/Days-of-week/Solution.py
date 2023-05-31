from datetime import datetime

cache = {}

def day_of_week(day, month, year):
    # Check if the date is already calculated before, return from cache if found.
    if (day, month, year) in cache:
        return cache[(day, month, year)]
    
    # Input validation
    try:
        date = datetime(year, month, day)
    except ValueError:
        return 'Invalid date'
        
    # We map the weekday() integer to its day name using a dictionary
    days = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
    }
    
    # Store the result into the cache before returning
    cache[(day, month, year)] = days[date.weekday()]
    return cache[(day, month, year)]
