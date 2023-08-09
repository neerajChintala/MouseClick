# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 15:56:15 2022
Updated on Wed Aug  9 16:05:06 2023
@author: Neeraj Chinthala
"""
import customtkinter as custtk

import threading

try:
    import pyautogui
except ImportError:
    try:
        import os
        import time
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

def labelConf(text):
    label.configure(text=text, fg_color='darkblue', text_color='white')
def looper(endTime):
    #def: function to automate the mouse click every 10 seconds till the time runs out
    #waiter = (datetime.now()).strftime('%H:%M:%S')
    while(True):
        timeNow = (datetime.now()).strftime('%H:%M:%S')
        if(timeNow < endTime):
            time.sleep(10)
            pyautogui.click(200, 500) #This defines where the click happens
        else:
            labelConf(text=f"\nFinished at {(datetime.now()).strftime('%H:%M:%S')} \n You can try to re-run with the same entry or enter new entry\n\nPS: If you want to exit, please press on EXIT to close the app.")
            break


custtk.set_appearance_mode("System")
custtk.set_default_color_theme("dark-blue")

root = custtk.CTk()
#root.protocol("WM_DELETE_WINDOW", root.iconify())
root.bind('<Escape>', lambda e: root.destroy())
root.geometry("500x350")

def close_app():
   root.destroy()
def validate(timeLeft):
    isNotValid = False
    if not timeLeft.isalpha():
        FMT = '%H:%M:%S'
        try:
            timeLeft = float(timeLeft)
        except ValueError:
            try:
                timeLeft = int(timeLeft)
            except ValueError:
                isNotValid = True
        finally:
            if isNotValid:
                labelConf(text=f"\nI couldn't convert {timeLeft} into a numerical value. \nPlease check it and re-run this!!", anchor='center')
            elif timeLeft > 0:
                currentTime, currentTimeF = (datetime.now()).strftime(FMT), datetime.now()
                endTimeList = (currentTimeF + timedelta(hours=(float(timeLeft)))).strftime(FMT).split(":")
                correctedSeconds = str(((int(endTimeList[2]) // 10) + 1) * 10)
                endTimeList.insert(2, correctedSeconds)
                endTimeList.pop(-1)
                endTime = ":".join(endTimeList)
                labelConf(text=f"Validated successfully!!! \nInception Time: {currentTime} \nTime left: {endTime} \n Executing...")
                looper(endTime)
            else:
                labelConf(text="\n I just can't execute it for 0 mins/seconds, right? \nPlease try again with proper input")
    else:
        labelConf(text=f"\nExpected values are int or floating point numerical. \n\n{message} \n\n")

def test():
    inp = entry1.get()
    labelConf(text="Provided Input: " + inp+"\n Validating and running")
    validate(inp)

frame = custtk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill='both', expand=True)

label = custtk.CTkLabel(master=frame, text='Test')#, text_font=('Roboto',24))
label.pack(padx=10,pady=12)
message = '''          
\tEnter timeleft            
'''+'''
Note:
If you want anything within an hour, please enter it in 0.XX.

If you don't wanna run this, press the EXIT button to end this

Example: 
    0.5 gives 1/2 hour
'''

labelConf(text=message)
entry1 = custtk.CTkEntry(master=frame, placeholder_text='test entry')
entry1.pack(padx=10,pady=12)

button = custtk.CTkButton(master=frame, text='Run', command = lambda: threading.Thread(target=test).start())
button.pack(padx=10, pady=12)
btn = custtk.CTkButton(master=root, text="EXIT", command=close_app).pack()

root.mainloop()
