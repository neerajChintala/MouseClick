# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 15:56:15 2022

@author: Neeraj Chinthala
"""
try:
    import pyautogui
except ImportError:
    try:
        os.system("pip install pyautogui")
        time.sleep(10)
        import pyautogui
    except ImportError:
        try:
            print("Trying to fetch pyautogui using conda")
            os.system("conda install pyautogui")
            time.sleep(10)
            import pyautogui
        except ImportError:
            print("error in fetching pyautogui")
finally:
    import time
    from datetime import datetime,timedelta
    import os

def looper(endTime):
    #def: function to automate the mouse click every 10 seconds till the time runs out
    #waiter = (datetime.now()).strftime('%H:%M:%S')
    while(True):
        timeNow = (datetime.now()).strftime('%H:%M:%S')
        if(timeNow < endTime):
            time.sleep(10)
            pyautogui.click(200, 500) #This defines where the click happens
        else:
            print(f"\nFinished at {(datetime.now()).strftime('%H:%M:%S')}")
            break

message = '''          
Enter timeleft            

Note:
If you want anything within an hour, please enter it in 0.XX.

If you don't wanna run this, enter "stop" to end this

Example: 
    0.5 gives 1/2 hour
'''
print(message)
timeleft = input("Enter time: ")
isNotValid = False
if not timeleft.isalpha():
    FMT = '%H:%M:%S'
    try:
        timeleft = float(timeleft)
    except ValueError:
        try:
            timeleft = int(timeleft)
        except ValueError:
            isNotValid = True
    finally:
        if isNotValid == True:
            print(f"\nI couldn't convert {timeleft} into a numerical value. \nPlease check it and re-run this!!")
        elif timeleft > 0:
            currentTime, currentTimeF  = (datetime.now()).strftime(FMT), datetime.now()
            endTimeList = (currentTimeF+timedelta(hours=(float(timeleft)))).strftime(FMT).split(":")
            correctedSeconds = str(((int(endTimeList[2])//10)+1)*10)
            endTimeList.insert(2, correctedSeconds)
            endTimeList.pop(-1)
            endTime = ":".join(endTimeList)
            print("\nInception Time:",currentTime, "\nTime left:", endTime)
            print("\n Executing...")
            looper(endTime)
        else:
            print("\n I just can't execute it for 0 mins/seconds, right?")
else:
    if(timeleft.lower() == "stop"):
        print("\nStopping")
    else:
        print("\nExpected values are int or floating point numerical. \n\nYou can also enter 'stop' to exit without any error. \n\nExiting...")
