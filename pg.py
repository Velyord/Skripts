import pyautogui as pg
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

print("Provide link for downloading: ")
doctor = input()

driver = webdriver .Chrome("C:\Program Files (x86)\chromedriver.exe")
driver.get(doctor)
a = ActionChains(driver)

def main():
    downloadSet()
    
    runDoc()
    #runDent()
    
    notify()
    driver.quit()
    
def downloadSet():
    time.sleep(1)
    with pg.hold('win'):
        pg.press('up')
    pg.press('enter')
    time.sleep(2)
    with pg.hold('ctrl'):
        pg.press('t')
    pg.write('chrome://settings/downloads')
    pg.press('enter')
    time.sleep(3)
    pg.press('tab', presses=3)
    pg.press('enter')
    with pg.hold('ctrl'):
        pg.press('w')
        
def runDoc(): 
    def runYearsDoc():
        runYearDoc("2022-2021", 1)
        runYearDoc("2022-2021", 2)
        runYearDoc("2020", 1)
        runYearDoc("2019", 1)
        runYearDoc("2018", 1)
        runYearDoc("2017", 1)
        runYearDoc("2016", 1)
        runYearDoc("2015-2014", 1)
    def runYearDoc(year, dyear):
        navigateYearDoc(year)
        setYearDoc(year, dyear)   
        runMonthsDoc()
    def navigateYearDoc(year):
        try:
            element = WDW(driver,300).until(EC.presence_of_element_located((By.LINK_TEXT,"Начало"))).click()
            element = WDW(driver,300).until(EC.presence_of_element_located((By.LINK_TEXT, year))).click()
            element = WDW(driver,300).until(EC.presence_of_element_located((By.LINK_TEXT, "Справки и отчети"))).click()
            element = WDW(driver,300).until(EC.presence_of_element_located((By.LINK_TEXT, "НЗОК"))).click()
            element = WDW(driver,300).until(EC.presence_of_element_located((By.LINK_TEXT, "Месечен отчет за РЗОК"))).click()
            element = WDW(driver,300).until(EC.presence_of_element_located((By.ID, "ctl00_CPH_SelectPeriod1_cbYEAR"))).click()
        finally: print("done!")
    def setYearDoc(year, dyear):
        pg.press('up', presses=7)
        if(year == "2022-2021" and dyear == 1):
            print("ok")
        elif(year == "2022-2021" and dyear == 2):
            pg.press('down', presses = 1)
        elif(year == "2020"):
            pg.press('down', presses = 2)
        elif(year == "2019"):
            pg.press('down', presses = 3)
        elif(year == "2018"):
            pg.press('down', presses = 4)
        elif(year == "2017"):
            pg.press('down', presses = 5)
        elif(year == "2016"):
            pg.press('down', presses = 6)
        else:
            pg.press('down', presses = 7)
        pg.press('enter')
    def runMonthsDoc():
        runMonthDoc("jan")
        runMonthDoc("feb")
        runMonthDoc("mar")
        runMonthDoc("apr")
        runMonthDoc("may")
        runMonthDoc("jun")
        runMonthDoc("jul")
        runMonthDoc("aug")
        runMonthDoc("sep")
        runMonthDoc("oct")
        runMonthDoc("nov")
        runMonthDoc("dec")
    def runMonthDoc(month):
        setMonthDoc(month)
        downloadMonthDoc()
    def setMonthDoc(month):
        try: # Месец
            element = WDW(driver,300).until(EC.presence_of_element_located((By.ID, "ctl00_CPH_SelectPeriod1_cbMONTH"))).click()
        finally: print("done!")
        pg.press('up', presses=12)

        if month == "jan":
            print("ok")
        elif month == "feb":
            pg.press('down', presses = 1)
        elif month == "mar":
            pg.press('down', presses = 2)
        elif month == "apr":
            pg.press('down', presses = 3)
        elif month == "may":
            pg.press('down', presses = 4)
        elif month == "jun":
            pg.press('down', presses = 5)
        elif month == "jul":
            pg.press('down', presses = 6)
        elif month == "aug":
            pg.press('down', presses = 7)
        elif month == "sep":
            pg.press('down', presses = 8)
        elif month == "oct":
            pg.press('down', presses = 9)
        elif month == "nov":
            pg.press('down', presses = 10)
        elif month == "dec":
            pg.press('down', presses = 11)

        pg.press('enter')
    def downloadMonthDoc():
        try:
            element = WDW(driver,300).until(EC.presence_of_element_located((By.ID, "ctl00_CPH_btnGen"))).click()
            a.move_to_element(driver.find_element("xpath", "//*[contains(text(), 'Генерирай отчет')]")).perform()
            a.move_to_element(driver.find_element("xpath", "//*[contains(text(), 'Текущ отчет')]")).click().perform()
            pg.press('end')
            element = WDW(driver,300).until(EC.presence_of_element_located((By.ID, "ctl00_CPH_btnEO"))).click()
            a.move_to_element(driver.find_element("xpath", "//*[contains(text(), 'Изтегли електронен отчет')]")).click().perform()
        finally: print("done!")
        time.sleep(2)
        pg.press('enter')
        pg.press('home')
        driver.back()
    runYearsDoc()    
def runDent():
    def runYearsDent():
        runYearDent("2020-2016", 20)
        runYearDent("2020-2016", 19)
        runYearDent("2020-2016", 18)
        runYearDent("2020-2016", 17)
        runYearDent("2020-2016", 16)
    def runYearDent(year, dyear):
        navigateYearDent(year)
        setYearDent(year, dyear)
        runMonthsDent()
    def navigateYearDent(year):
        try:
            element = WDW(driver,300).until(EC.presence_of_element_located((By.LINK_TEXT,"Пациенти"))).click()
            element = WDW(driver,300).until(EC.presence_of_element_located((By.LINK_TEXT, year))).click()
            element = WDW(driver,300).until(EC.presence_of_element_located((By.LINK_TEXT, "Месечен отчет за РЗОК"))).click()
            element = WDW(driver,300).until(EC.presence_of_element_located((By.LINK_TEXT, "Месечен отчет на лекаря"))).click()
            element = WDW(driver,300).until(EC.presence_of_element_located((By.ID, "ctl00_CPH_SelectPeriod1_cbYEAR"))).click()
        finally: print("done!")
    def setYearDent(year, dyear):
        pg.press('up', presses=7)
        if(year == "2020-2016" and dyear == 20):
            pg.press('down', presses = 2)
        elif(year == "2020-2016" and dyear == 19):
            pg.press('down', presses = 3)
        elif(year == "2020-2016" and dyear == 18):
            pg.press('down', presses = 4)
        elif(year == "2020-2016" and dyear == 17):
            pg.press('down', presses = 5)
        else:
            pg.press('down', presses = 6)
        pg.press('enter')
    def runMonthsDent():
        runMonthDent("jan")
        runMonthDent("feb")
        runMonthDent("mar")
        runMonthDent("apr")
        runMonthDent("may")
        runMonthDent("jun")
        runMonthDent("jul")
        runMonthDent("aug")
        runMonthDent("sep")
        runMonthDent("oct")
        runMonthDent("nov")
        runMonthDent("dec")
    def runMonthDent(month):
        setMonthDent(month)
        downloadMonthDent()
    def setMonthDent(month):
        try: # Месец
            element = WDW(driver,300).until(EC.presence_of_element_located((By.ID, "ctl00_CPH_SelectPeriod1_cbMONTH"))).click()
        finally: print("done!")
        pg.press('up', presses=12)

        if month == "jan":
            print("ok")
        elif month == "feb":
            pg.press('down', presses = 1)
        elif month == "mar":
            pg.press('down', presses = 2)
        elif month == "apr":
            pg.press('down', presses = 3)
        elif month == "may":
            pg.press('down', presses = 4)
        elif month == "jun":
            pg.press('down', presses = 5)
        elif month == "jul":
            pg.press('down', presses = 6)
        elif month == "aug":
            pg.press('down', presses = 7)
        elif month == "sep":
            pg.press('down', presses = 8)
        elif month == "oct":
            pg.press('down', presses = 9)
        elif month == "nov":
            pg.press('down', presses = 10)
        elif month == "dec":
            pg.press('down', presses = 11)

        pg.press('enter')
    def downloadMonthDent():
        try:
            element = WDW(driver,300).until(EC.presence_of_element_located((By.ID, "ctl00_CPH_btnGen"))).click()
            pg.press('end')
            element = WDW(driver,300).until(EC.presence_of_element_located((By.ID, "ctl00_CPH_btnEO"))).click()
        finally: print("done!")
        time.sleep(2)
        pg.press('enter')
        pg.press('home')
        driver.back()

def notify():
    with pg.hold('ctrl'):
        pg.press('t')
    pg.write('facebook.com')
    pg.press('enter')
    time.sleep(5)
    pg.press('enter')
    time.sleep(2)
    pg.write('your.mail@gmail.com')
    pg.press('tab', presses=2)
    pg.write('yourpassword')
    pg.press('enter')
    time.sleep(10)
    pg.press('tab', presses=10)
    pg.press('enter')
    time.sleep(5)
    pg.press('tab', presses=5)
    pg.press('enter')
    time.sleep(5)
    pg.write('done! Boss')
    pg.press('enter')
    time.sleep(1)

main()