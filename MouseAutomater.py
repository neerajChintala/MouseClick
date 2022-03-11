# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 15:56:15 2022

@author: Neeraj Chinthala
"""
try:
    import pyautogui
    import time
    from datetime import datetime,timedelta
    import os
except ImportError:
    try:
        os.system("pip install pyautogui")
        time.sleep(10)
        import pyautogui
    except:
        try:
            print("Trying to fetch pyautogui using conda")
            os.system("conda install pyautogui")
            time.sleep(10)
            import pyautogui
        except:
            print("error in fetching pyautogui")

def looper(endTime):
    #def: function to automate the mouse click every 10 seconds till the time runs out
    #desiredTime = (datetime.now()).strftime('%H:%M:%S')
    waiter = (datetime.now()).strftime('%H:%M:%S')
    k = int(waiter.split(":")[2])
    time.sleep(abs(int(waiter.split(":")[2])-((k//10)+1)* 10))
    while(True):
        print((datetime.now()).strftime('%H:%M:%S'), endTime,(datetime.now()).strftime('%H:%M:%S') != endTime)
        timeNow = (datetime.now()).strftime('%H:%M:%S')
        print(timeNow[0]==endTime[0] and timeNow[0]==endTime[0] and int(timeNow[0]) >= int(endTime[0]))
        if((datetime.now()).strftime('%H:%M:%S') != endTime):
            time.sleep(10)
            pyautogui.click(200, 500) #This defines where the click happens
        else:
            print("Finished")
            break
message = '''          
Enter timeleft            

Note:
If you want anything within an hour, please enter it in 0.XX.

If you don't wanna run this, enter stop to end this

Example: 
    0.5 gives 1/2 hour
'''
print(message)
timeleft = input("Enter time: ")
if not timeleft.isalpha():
    FMT = '%H:%M:%S'
    try:
        timeleft = float(timeleft)
    except:
        timeleft = int(timeleft)
    finally:
        currentTime = (datetime.now()).strftime(FMT)
        currentTimeF = datetime.now()
        endTimeList = (currentTimeF+timedelta(hours=(float(timeleft)))).strftime(FMT).split(":")
        correctedSeconds = str(((int(endTimeList[2])//10)+1)*10)
        endTimeList.insert(2, correctedSeconds)
        endTimeList.pop(-1)
        endTime = ":".join(endTimeList)
        print("Time Now:",currentTime, "; Time left:", endTime)
        print("\n Executing...")
        looper( endTime)
else:
    if(timeleft.lower() == "stop"):
        print("\nStopping")
    else:
        print("\nExpected values must be an int or floating point numerical. \n\nYou can also enter 'stop' to exit without any error. \n\nExiting")
    



