import datetime
import schedule
import time
#import keyboard  
from selenium import webdriver
from info import *
from join import *

#pip install -r requirements.txt

datelog = datetime.datetime.now()
day = (datelog.strftime("%a"))
print(day)

currentTime = datelog.strftime("%H:%M:%S")
print("time:", currentTime)


''' monday'''
schedule.every().monday.at(firstClass).do(joinCY)
schedule.every().monday.at(secondClass).do(joinMAD)
schedule.every().monday.at(thirdClass).do(joinSC)
schedule.every().monday.at(fourthClass).do(joinDWDM)
schedule.every().monday.at(fifthClass).do(joinST)
    
'''tuesday'''
schedule.every().tuesday.at(firstClass).do(joinCY)
schedule.every().tuesday.at(secondClass).do(joinDWDM)
schedule.every().tuesday.at(thirdClass).do(joinST)
schedule.every().tuesday.at(fourthClass).do(joinMEPA)
schedule.every().tuesday.at(fifthClass).do(joinSC)

'''wednesday'''
schedule.every().wednesday.at(firstClass).do(joinCY)
schedule.every().wednesday.at(secondClass).do(joinSC)
schedule.every().wednesday.at(thirdClass).do(joinMAD)
schedule.every().wednesday.at(fourthClass).do(joinDWDM)
schedule.every().wednesday.at(fifthClass).do(joinST)

'''thursday'''
schedule.every().thursday.at(firstClass).do(joinCY)
schedule.every().thursday.at(secondClass).do(joinMAD)
schedule.every().thursday.at(thirdClass).do(joinSC)
schedule.every().thursday.at(fourthClass).do(joinMEPA)
schedule.every().thursday.at(fifthClass).do(joinDWDM)

'''friday'''
schedule.every().friday.at(firstClass).do(joinMEPA)
schedule.every().friday.at(secondClass).do(joinDWDM)
schedule.every().friday.at(thirdClass).do(joinST)
schedule.every().friday.at(fourthClass).do(joinST)
schedule.every().friday.at(fifthClass).do(joinMAD)

while True:
    schedule.run_pending()
    time.sleep(1) 

