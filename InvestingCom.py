from matplotlib import image
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
from datetime import datetime

from PIL import Image, ImageDraw, ImageFont

sline =[]
sticker =[]
PATH = "C:\DEV\Python\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.set_window_size(1300,1900);


# opening the CSV file 
with open('borsa.csv', mode ='r')as file: 
      
  # reading the CSV file 
  csvFile = csv.reader(file) 
    
  # displaying the contents of the CSV file 
  for lines in csvFile: 
        print(lines[2]) 
        sline.append(lines)
        sticker.append(lines[2])
print("list done")




linkpath = "https://www.investing.com/equities/marathon-petroleum-corp." 
driver.get(linkpath)
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 2)
time.sleep(2)

btnall = driver.find_elements(By.CLASS_NAME, "chart-button ")
for btn in btnall:
    print(btn.get_attribute("title"))
    if btn.get_attribute("title") == "Candlestick Chart":
        btn.click()

time.sleep(25)                                              
el = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[2]/div/div/div[2]/main/div/div[7]/div/div[1]/div/div[2]/div/cq-context/div[2]/div[2]/canvas[2]")))
el.screenshot('C:\\DEV\\Python\\Datasets\\i-1d.png')


btnallA = driver.find_elements(By.TAG_NAME, "button")
for btn in btnallA:    
    if btn.text == "1 Week":
        btn.click()
        break
time.sleep(9)
el = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[2]/div/div/div[2]/main/div/div[7]/div/div[1]/div/div[2]/div/cq-context/div[2]/div[2]/canvas[2]")))
el.screenshot('C:\\DEV\\Python\\Datasets\\i-1w.png')       
        
        
btnallB = driver.find_elements(By.TAG_NAME, "button")
for btn in btnallB:   
    if btn.text == "1 Month":
        btn.click()
        break
time.sleep(6)
el = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[2]/div/div/div[2]/main/div/div[7]/div/div[1]/div/div[2]/div/cq-context/div[2]/div[2]/canvas[2]")))
el.screenshot('C:\\DEV\\Python\\Datasets\\i-1m.png')       


        
btnallC = driver.find_elements(By.TAG_NAME, "button")
for btn in btnallC:   
    if btn.text == "6 Month":
        btn.click()
        break
time.sleep(6)
el = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[2]/div/div/div[2]/main/div/div[7]/div/div[1]/div/div[2]/div/cq-context/div[2]/div[2]/canvas[2]")))
el.screenshot('C:\\DEV\\Python\\Datasets\\i-6m.png')       












#Write csv
# field names 
#fields = ['No', 'ticker', 'company', 'sector', 'industuri'] 
    
# data rows of csv file 
rows = [sline[3] ] 
    
# name of csv file 
filename = "borsa.csv"
    
# writing to csv file 
with open(filename, 'a', newline='') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # writing the fields 
    #csvwriter.writerow(fields) 
        
    # writing the data rows 
    csvwriter.writerows(rows)
        