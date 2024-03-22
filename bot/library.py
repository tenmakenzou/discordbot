from datetime import datetime

def get_library():
    current_date = datetime.now()
    day_of_week = current_date.weekday()  
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    x = days_of_week[day_of_week]
    current_hour = current_date.hour 
    
    current_time = float(current_date.strftime("%H.%M"))
    if (9.00 <= current_time <= 19.00) and (x != 'Friday') and (x != 'Saturday') and (x != 'Sunday'):
        return "**Η Βιβλιοθήκη είναι ανοιχτή**"
    elif (9.00 <= current_time <= 15.30) and (x == 'Friday') and (x != 'Saturday') and (x != 'Sunday'):
        return "**Η Βιβλιοθήκη είναι ανοιχτή**"
    else:
        return "**Η Βιβλιοθήκη είναι κλειστή**"

