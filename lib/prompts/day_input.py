def day_input():
    valid_numbers = [1, 2, 3, 4, 5, 6, 7]
    workout_days = input("How many days would you like to work out per week? ")
    if int(workout_days) in valid_numbers:
        return int(workout_days)
    else:
        print("Please select at least 1 day and up to 7 days")
        return day_input()