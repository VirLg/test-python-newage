import gspread
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time

URL = 'https://www.olx.ua/uk/nedvizhimost/kvartiry/'

service = Service()

def getCodeWithOlx(URL: str):
    driver = webdriver.Chrome(service=service)
    try:
        driver.get(URL)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "css-1ohf0ui"))).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "css-1sw7q4x"))).click()
        time.sleep(4)
        
        price_element = driver.find_element(By.CLASS_NAME, "css-12vqlj3")
        price = price_element.text
        print("Price:", price)

        float_element = driver.find_element(By.XPATH, "//p[contains(text(), 'Поверх')]")
        floor = float_element.text
        print("Float:", floor)

        floating_element = driver.find_element(By.XPATH, "//p[contains(text(), 'Поверховість')]")
        floating = floating_element.text
        print("Floating:", floating)

        square_element = driver.find_element(By.XPATH, "//p[contains(text(), 'Загальна площа')]")
        square = square_element.text
        print("Square:", square)

        location_element = driver.find_element(By.CLASS_NAME, "css-1cju8pu")
        location = location_element.text
        print("Location:", location)

        return {
            "Price": price,
            "Float": floor,
            "Floating": floating,
            "Square": square,
            "Location": location
        }
    finally:
        driver.quit()

ds = getCodeWithOlx(URL)
gc = gspread.service_account(filename='creds.json')
wks = gc.open("test")
worksheet = wks.worksheet("Task3")

worksheet.append_row([ds[key] for key in ds])