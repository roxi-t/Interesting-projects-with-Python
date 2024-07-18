import time
# برای حذف تایم های قبلی 
from os import system , name
while True :
    Choice = input("Do you want to start ? (y/n) : ")
    if 'y' in Choice.lower():
        hour = int(input("Enter hour : "))
        minuts = int(input("Enter minuts : "))
        second = int(input("Enter second : "))
        total = hour * 60 * 60 +minuts *60 + second
        print("Timers Start now ... ")
        time.sleep(1)
        while total > 1 :
            print(total)
            total -=1
            time.sleep(1)
            if name == "nt":
                system("cls")
            else :
                system("clear")
        print("Timer ended .... ")
    elif 'n' in Choice.lower():
        print("Exiting ....")
        break
    else :
        print("invalid input ... ")
