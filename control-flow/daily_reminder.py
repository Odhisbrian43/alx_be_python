#Daily task reminded script

task = input("Enter your task: ")
priority = ("Priority (high/medium/low): ")
time = ("Is it time-bound? (yes/no): ")

for i in ["high", "medium", "low"]:
    match priority:
        case "i"
        if time == "yes":
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
        elif time == "no":
            print(f"Note: {task} needs your attention but you can do it when you have time.")
        else:
            print("Invalid input.")

