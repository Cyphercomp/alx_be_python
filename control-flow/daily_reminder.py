task = input("Enter your task:")
time_bound = input("is it time_bound-bound? (yes/no)")
priority = input ("Priority (high/medium/low):")


match priority :
    case "high" :
        if time_bound == "yes" :
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else :
            print(f"Note: '{task}' is a high priority task that requires immediate attention today!")   
    case "medium" :
        if time_bound == "yes" :
            print(f"Reminder: '{task}' is a medium priority task that requires  attention today!")
        else :
            print(f"Note: '{task}' is a medium priority task that requires  attention today!") 
    case "low" :
        if time_bound == "yes" :
            print(f"Reminder: '{task}' is a  low priority task. Consider completing it when you have free time_bound.")
        else :
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time_bound.") 
    case _:
        print("Invalid day entered.")