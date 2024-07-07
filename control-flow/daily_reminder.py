Task = input("Enter your Task:")
Time_bound = input("is it Time_bound-bound? (yes/no)")
Priority = input ("Priority (high/medium/low):")


match Priority :
    case "high" :
        if Time_bound == "yes" :
            print(f"Reminder: '{Task}' is a high Priority Task that requires immediate attention today!")
        else :
            print(f"Note: '{Task}' is a high Priority Task that requires immediate attention today!")   
    case "medium" :
        if Time_bound == "yes" :
            print(f"Reminder: '{Task}' is a medium Priority Task that requires  attention today!")
        else :
            print(f"Note: '{Task}' is a medium Priority Task that requires  attention today!") 
    case "low" :
        if Time_bound == "yes" :
            print(f"Reminder: '{Task}' is a  low Priority Task. Consider completing it when you have free Time_bound.")
        else :
            print(f"Note: '{Task}' is a low Priority Task. Consider completing it when you have free Time_bound.") 
    case _:
        print("Invalid day entered.")