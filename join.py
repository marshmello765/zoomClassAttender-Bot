from info import *
from selenium import webdriver
import time


def joinMAD():
    driver = webdriver.Chrome('C:/Users/damas/Desktop/codes/Zoom-Bot/chromedriver.exe')
    driver.get(MAD)
    time.sleep(100) #seconds
    zoomJoin()
    time.sleep(3000)
    driver.quit()

def joinSC():
    driver = webdriver.Chrome('C:/Users/damas/Desktop/codes/Zoom-Bot/chromedriver.exe')
    driver.get(SC)
    time.sleep(100) #seconds
    zoomJoin()
    time.sleep(3000)
    driver.quit()

def joinMEPA():
    driver = webdriver.Chrome('C:/Users/damas/Desktop/codes/Zoom-Bot/chromedriver.exe')
    driver.get(MEPA)
    time.sleep(100) #seconds
    zoomJoin()
    time.sleep(3000)
    driver.quit()

def joinDWDM():
    driver = webdriver.Chrome('C:/Users/damas/Desktop/codes/Zoom-Bot/chromedriver.exe')
    driver.get(DWDM)
    time.sleep(100) #seconds
    zoomJoin()
    time.sleep(3000)
    driver.quit()

def joinST():
    driver = webdriver.Chrome('C:/Users/damas/Desktop/codes/Zoom-Bot/chromedriver.exe')
    driver.get(ST)
    time.sleep(100) #seconds
    zoomJoin()
    time.sleep(3000)
    driver.quit()

def joinCY():
    driver = webdriver.Chrome('C:/Users/damas/Desktop/codes/Zoom-Bot/chromedriver.exe')
    driver.get(CY)
    time.sleep(100) #seconds
    zoomJoin()
    time.sleep(3000)
    driver.quit()










def zoomJoin():
    print("inside zoom")