from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService 
#from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def getDataAndDate():
    user_name='m.nelson@choosevantage.com'
    password='Marty1!'
    options = webdriver.ChromeOptions()
    options.headless = True
    DRIVER_PATH = r'C:\chromedriver_win32\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=DRIVER_PATH,options=options)
    driver.get('https://panel.solarhub.io/admin/users/login')
    sleep(2)
    username = driver.find_element(By.ID,"UserEmail").send_keys(user_name)
    sleep(1)
    pwd = driver.find_element(By.ID,"UserPassword").send_keys(password)
    sleep(1)
    click = driver.find_element(By.CLASS_NAME,'submit').submit()
    sleep(3)
    financial = driver.find_element(By.XPATH,"/html/body/header/a[5]")
    print(financial.is_displayed)
    financial.click()
    sleep(3)
    excel_data = driver.find_element(By.XPATH,"/html/body/main/div/div/table/tbody/tr[1]/td[1]/a")
    excel_data.click()
    sleep(5)
    date=driver.find_element(By.XPATH,"/html/body/main/div/div/table/tbody/tr[1]/td[2]").text
    date= pd.to_datetime(date)
    date= date.strftime("%u")
    return date
    sleep(3)
d= getDataAndDate()
print('week',d)


