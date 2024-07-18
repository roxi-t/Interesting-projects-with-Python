import time
# To clear previous outputs
from os import system, name

while True:
    # Prompt the user to start the timer
    Choice = input("Do you want to start? (y/n): ")
    if 'y' in Choice.lower():
        # Get the timer duration from the user
        hour = int(input("Enter hour: "))
        minutes = int(input("Enter minutes: "))
        second = int(input("Enter seconds: "))
        
        # Calculate the total time in seconds
        total = hour * 60 * 60 + minutes * 60 + second
        
        print("Timer starts now...")
        time.sleep(1)
        
        # Countdown loop
        while total > 1:
            print(total)
            total -= 1
            time.sleep(1)
            
            # Clear the screen based on the operating system
            if name == "nt":
                system("cls")
            else:
                system("clear")
        
        print("Timer ended...")
    
    elif 'n' in Choice.lower():
        # Exit the program if user chooses 'n'
        print("Exiting...")
        break
    
    else:
        # Handle invalid input
        print("Invalid input...")
