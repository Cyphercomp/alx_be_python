task = input("Enter your task:")
priority = input ("Priority (high/medium/low):")
time = input("is it time-bound? (yes/no)")

match priority :
    case "high" :
        if time == "yes" :
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else :
            print(f"Note: '{task}' is a high priority task that requires immediate attention today!")   
    case "medium" :
        if time == "yes" :
            print(f"Reminder: '{task}' is a medium priority task that requires  attention today!")
        else :
            print(f"Note: '{task}' is a medium priority task that requires  attention today!") 
    case "low" :
        if time == "yes" :
            print(f"Reminder: '{task}' is a  low priority task. Consider completing it when you have free time.")
        else :
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.") 
    case _:
        print("Invalid day entered.")