import time
human_detect = False
light = False
door_lock = True
log_filename = "system_log.txt"
#Dictionary
kitchen_menu_data = {
    "Monday": {"Breakfast": "Tea & Toasted Bread", "Lunch": "Chicken Biryani", "Dinner": "Chicken Roast"},
    "Tuesday": {"Breakfast": "Fresh Juice & Omelet", "Lunch": "Shami Kabab with Naan", "Dinner": "Italian Pizza"},
    "Wednesday": {"Breakfast": "Tea & Paratha", "Lunch": "BBQ Platter", "Dinner": "Chicken Karahi"},
    "Thursday": {"Breakfast": "Fruit Juice & Pancakes", "Lunch": "Mixed Vegetable Curry", "Dinner": "Vegetable Chow Mein"},
    "Friday": {"Breakfast": "Tea & French Toast", "Lunch": "Special Biryani", "Dinner": "Grilled Chicken"},
    "Saturday": {"Breakfast": "Tea & Omelet", "Lunch": "Chicken Biryani", "Dinner": "Chicken Roast"},
    "Sunday": {"Breakfast": "Fresh Juice & Halwa Puri", "Lunch": "Fast Food Combo", "Dinner": "Chicken Spaghetti"}
}
# File Handling
def log_event(message):
    file = open(log_filename, "a")
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    file.write("[" + timestamp + "] " + message + "\n")
    file.close()
    
def get_user_choice(prompt="Please enter choice: "):
    choice = input(prompt)
    while not choice.isdigit():
        print("Invalid input! Please enter a valid number.")
        choice = input(prompt)
    return int(choice)

def adjust_light():
    current_time_struct = time.localtime()
    hour = current_time_struct.tm_hour
    print("\nCurrent system time: " + time.strftime("%I:%M %p"))
    if 6 <= hour < 18:
        intensity = 100
    elif 18 <= hour < 22:
        intensity = 50
    else:
        intensity = 20
    print("Intensity automatically adjusted to " + str(intensity) + "%")
    log_event("Light intensity auto-adjusted to " + str(intensity) + "%")

def human_detection():
    global human_detect, door_lock, light
    if human_detect:
        door_lock = False
        light = True
        print("Human detected")
        print("Door unlocked")
        print("Lights on")
        log_event("Human detected - Door unlocked, Lights on")
        adjust_light()
    else:
        door_lock = True
        light = False
        print("No Human detection")
        print("Door locked")
        print("Light off")
        log_event("No Human detected - Door locked, Lights off")

def control_temperature():
    while True:
        print("\nTemperature control")
        print("1. Cold temperature")
        print("2. Normal temperature")
        print("3. Hot temperature")
        print("4. Exit system")
        choice = get_user_choice()
        if choice == 1:
            print("Temperature decreased")
            log_event("Temperature decreased")
        elif choice == 2:
            print("Normal temperature adjusted")
            log_event("Temperature set to normal")
        elif choice == 3:
            print("Temperature increased")
            log_event("Temperature increased")
        elif choice == 4:
            break
        else:
            print("Invalid choice")

def kitchen_menu():
    while True:
        print("\n1. For showing full weekly menu")
        print("2. For showing TODAY'S menu")
        print("3. Exit")
        choice = get_user_choice()
        if choice == 1:
            for day in kitchen_menu_data:
                print("On " + day + " the Menu is:")
                day_menu = kitchen_menu_data[day]
                for meal_type in day_menu:
                    dish = day_menu[meal_type]
                    print("." + meal_type + ":" + dish)
                print()
            log_event("Full weekly kitchen menu viewed")
        elif choice == 2:
            today = time.strftime("%A")
            print("\nToday is " + today + ". Today's Menu:")     
            if today in kitchen_menu_data:
                today_menu = kitchen_menu_data[today]
                for meal_type in today_menu:
                    dish = today_menu[meal_type]
                    print("- " + meal_type + ": " + dish)
            else:
                print("No menu found for today.")
                
            log_event("Today's menu (" + today + ") viewed")
        elif choice == 3:
            break
        else:
            print("Invalid choice")

def home_appliances_system():
    while True:
        print("\n1. Turn on washing machine")
        print("2. Turn on dryer")
        print("3. Turn on TV")
        print("4. Turn off TV")
        print("5. Turn on Dishwasher")
        print("6. Oven")
        print("7. Exit appliances system")
        choice = get_user_choice()
        if choice == 1:
            count1 = 16
            time.sleep(0.5)
            print("Washing machine turned on for " + str(count1) + " minutes")
            log_event("Washing machine turned on for " + str(count1) + " min")
        elif choice == 2:
            count2 = 16
            time.sleep(0.5)
            print("Dryer turned on for " + str(count2) + " minutes")
            log_event("Dryer turned on for " + str(count2) + " min")
        elif choice == 3:
            print("TV turned on")
            log_event("TV turned on")
        elif choice == 4:
            print("TV turned off")
            log_event("TV turned off")
        elif choice == 5:
            count3 = 16
            time.sleep(0.5)
            print("Dishwasher turned on for " + str(count3) + " minutes")
            log_event("Dishwasher turned on for " + str(count3) + " min")
        elif choice == 6:
            count4 = get_user_choice("Please enter minutes in number: ")
            time.sleep(0.5)
            print("Oven turned on for " + str(count4) + " minutes")
            log_event("Oven turned on for " + str(count4) + " min")
        elif choice == 7:
            break
        else:
            print("Invalid choice")


def security_system():
    motion_detect = False
    alarm_on = False
    door_locked = True

    while True:
        print("\n1. Detect unknown motion")
        print("2. Door unlock")
        print("3. Exit security system")

        choice = get_user_choice()

        if choice == 1:
            motion_detect = True
            alarm_on = True
            print("Motion detected! Alarm triggered")
            log_event("SECURITY ALERT: Motion detected! Alarm triggered")
        elif choice == 2:
            door_locked = False
            alarm_on = True
            print("Door unlocked! Alarm beeping")
            log_event("SECURITY ALERT: Door unlocked! Alarm beeping")
        elif choice == 3:
            break
        else:
            print("Invalid choice")
print("****SMART HOME AUTOMATION SYSTEM****")
while True:
    print("\n1. Human detection")
    print("2. Automation system off")
    options = get_user_choice()

    if options == 1:
        human_detect = True
        human_detection()

        while True:
            print("\n1. For Controlling temperature")
            print("2. For Kitchen menu per week")
            print("3. Enter appliances system")
            print("4. Security system")
            print("5. Exiting inner functions")

            choice = get_user_choice()
            if choice == 1:
                control_temperature()
            elif choice == 2:
                kitchen_menu()
            elif choice == 3:
                home_appliances_system()
            elif choice == 4:
                security_system()
            elif choice == 5:
                break
            else:
                print("Invalid option. Please try again.")

    elif options == 2:
        print("System off")
        log_event("Automation system turned OFF")
        break
    else:
        print("Invalid choice")
