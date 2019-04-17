# 
def return_day(day):
    weekdays = {1: "Monday", 
                2: "Tuesday",
                3: "Wednesday",
                4: "Thursday",
                5: "Friday",
                6: "Saturday",
                7: "Sunday"}
 
    today = weekdays.get(day)
    
    if today:
        return today
    return None
 
print(return_day(8))