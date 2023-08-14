def select_days(day_number):
    days = []
    
    while len(days) < day_number:
        day = check_proper_day()
        days.append(day)
    ordered_days = sorted(days, key=lambda day: day[1])
    return ordered_days

def check_proper_day():
    proper_days = {
            "sunday": 1,
            "monday": 2,
            "tuesday": 3,
            "wednesday": 4,
            "thursday": 5,
            "friday": 6,
            "saturday": 7
        }
    prompt = "Enter which days of the week you'd like to work out. "
    day = input(prompt)
    if proper_days[day] != None:
        return [day, proper_days[day]]
    else:
        print("please input a valid day: sunday, monday, etc. ")
        return check_proper_day()