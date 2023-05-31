from matplotlib import image
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

import pandas as pd
from pytrends.request import TrendReq


PATH = "C:\DEV\Python\chromedriver.exe"


sline =[]
d1 = []
d2 = []
d3 =[]
d4 = []
d5 =[]
d6 = []
d7 = []


filename = "borsa.csv"
candleFlag = "nope"

# opening the CSV file 
with open(filename, mode ='r')as file: 
      
  # reading the CSV file 
  csvFile = csv.reader(file) 
    
  # displaying the contents of the CSV file 
  for lines in csvFile:
      if lines[0] == "no":
          #print(lines)
          sline.append(lines)
          d1.append(lines[0])
          d2.append(lines[1])      
          d3.append(lines[2])
          d4.append(lines[3])
          d5.append(lines[4])
          d6.append(lines[5])
          d7.append(lines[6])                              
                    
print("list done")

driver = webdriver.Chrome(PATH)
driver.set_window_size(1300,1000);


for x in range(4990):
    print(sline[x])
    print(d3[x])

    linkpath = "https://finance.yahoo.com/quote/" + d3[x] 
    driver.get(linkpath)
    driver.implicitly_wait(10)
    wait = WebDriverWait(driver, 2)
    time.sleep(1)

    #btnall = driver.find_elements(By.CLASS_NAME, "chart-button ")
    #for btn in btnall:
    #    print(btn.get_attribute("title"))
    #    if btn.get_attribute("title") == "Candlestick Chart":
    #        btn.click()

    cname = "/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[6]/div/div/div/div[2]/div[1]/div[1]/h1"
    el = wait.until(EC.visibility_of_element_located((By.XPATH, cname)))
    compname = el.text

    prc = "/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[6]/div/div/div/div[3]/div[1]/div[1]/fin-streamer[1]"
    el = wait.until(EC.visibility_of_element_located((By.XPATH, prc)))
    price = el.text

    yuzde = "/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[6]/div/div/div/div[3]/div[1]/div[1]/fin-streamer[3]/span"
    el = wait.until(EC.visibility_of_element_located((By.XPATH, yuzde)))
    degisim = el.text

    once = "/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/div/div[2]/div[1]/table/tbody/tr[1]/td[2]"
    el = wait.until(EC.visibility_of_element_located((By.XPATH, once)))
    onceki = el.text

    vol = "/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/div/div[2]/div[1]/table/tbody/tr[7]/td[2]/fin-streamer"
    el = wait.until(EC.visibility_of_element_located((By.XPATH, vol))) 
    volume = el.text

    Avgvol = "/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/div/div[2]/div[1]/table/tbody/tr[8]/td[2]"
    el = wait.until(EC.visibility_of_element_located((By.XPATH, Avgvol)))
    Avgvolume = el.text
    
    #================Google tren Call ============================
    #print(d3[x])
    #coname = d4[x].replace("."," ").replace(",","")
    #pytrends = TrendReq(hl='en-US', tz=360)
    #pytrends.build_payload(kw_list=[coname], timeframe='now 7-d',geo='US', gprop='' )
    #df = pytrends.interest_over_time()
    #print(df['NYSE:UPS'])
    #ypoints = np.array(df[coname])
    #plt.figure(figsize=(9,1))
    #plt.plot(ypoints)
    #plt.savefig('C:\\DEV\\Python\\Datasets\\fig.png', dpi=100)
    #plt.show()
    #plt.close()
    
    
    
    

    if candleFlag =="nope":
        xx ="/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/div/div[1]/div/ul/li[9]/div/div"
        driver.find_element(By.XPATH, xx).click()
        time.sleep(2)
        #Cande chart Select 
        xx ="/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/div/div[1]/div/ul/li[9]/div/div[2]/ul/li[4]/button"
        driver.find_element(By.XPATH, xx).click()
        candleFlag = "ok"

    scrtake = "/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/div/div[1]/div/div[1]/canvas[2]"
    
    try:
        el = wait.until(EC.visibility_of_element_located((By.XPATH, scrtake)))
        el.screenshot('C:\\DEV\\Python\\Datasets\\y-1d.png')


        btn = "/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/div/div[1]/div/ul/li[2]/button"
        btnshow = wait.until(EC.visibility_of_element_located((By.XPATH, btn)))
        btnshow.click()
        #driver.find_element(By.XPATH, btn).click()                                            
        time.sleep(1)    
        el = wait.until(EC.visibility_of_element_located((By.XPATH, scrtake)))
        el.screenshot('C:\\DEV\\Python\\Datasets\\y-5d.png')

        btn = "/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/div/div[1]/div/ul/li[3]/button"
        #driver.find_element(By.XPATH, btn).click()
        btnshow = wait.until(EC.visibility_of_element_located((By.XPATH, btn)))
        btnshow.click()
        time.sleep(1)                                             
        el = wait.until(EC.visibility_of_element_located((By.XPATH, scrtake)))
        el.screenshot('C:\\DEV\\Python\\Datasets\\y-1m.png')

        btn = "/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/div/div/div/div[1]/div/ul/li[4]/button"
        btnshow = wait.until(EC.visibility_of_element_located((By.XPATH, btn)))
        btnshow.click()
        time.sleep(1)                                                   
        el = wait.until(EC.visibility_of_element_located((By.XPATH, scrtake)))
        el.screenshot('C:\\DEV\\Python\\Datasets\\y-6m.png')

        Master = Image.open('C:\\DEV\\Python\\Datasets\\master.png') 
        Mastercopy = Master.copy()
        Image1 = Image.open('C:\\DEV\\Python\\Datasets\\masterclean.png')
        Image1copy = Image1.copy() 
        Mastercopy.paste(Image1copy, (0, 0)) 
        Mastercopy.save('C:\\DEV\\Python\\Datasets\\master.png')  


        im = Image.open('C:\\DEV\\Python\\Datasets\\y-1d.png')
        im1 = im.crop((0,0,360,200))
        #im1.show()
        im1.save("C:\\DEV\\Python\\Datasets\\1d.png")
        time.sleep(1)    
        im = Image.open('C:\\DEV\\Python\\Datasets\\y-5d.png')
        im1 = im.crop((0,0,360,200))
        #im1.show()
        im1.save("C:\\DEV\\Python\\Datasets\\5d.png")
        im = Image.open('C:\\DEV\\Python\\Datasets\\y-1m.png')
        im1 = im.crop((0,0,360,200))
        #im1.show()
        im1.save("C:\\DEV\\Python\\Datasets\\1m.png")

        im = Image.open('C:\\DEV\\Python\\Datasets\\y-6m.png')
        im1 = im.crop((0,0,360,200))
        #im1.show()
        im1.save("C:\\DEV\\Python\\Datasets\\6m.png")  
        
        #im = Image.open('C:\\DEV\\Python\\Datasets\\fig.png')
        #im1 = im.crop((113,12,810,89))
        #im1.show()
        #im1.save("C:\\DEV\\Python\\Datasets\\trend.png") 
        
        
    
        Master = Image.open('C:\\DEV\\Python\\Datasets\\master.png') 
        Mastercopy = Master.copy()
        Image1 = Image.open('C:\\DEV\\Python\\Datasets\\1d.png')
        Image1copy = Image1.copy() 
        # paste image giving dimensions
        Image2 = Image.open('C:\\DEV\\Python\\Datasets\\5d.png')
        Image2copy = Image2.copy()     
        Image3 = Image.open('C:\\DEV\\Python\\Datasets\\1m.png')
        Image3copy = Image3.copy() 
        Image4 = Image.open('C:\\DEV\\Python\\Datasets\\6m.png')
        Image4copy = Image4.copy()   
        #Image5 = Image.open('C:\\DEV\\Python\\Datasets\\trend.png')
        #Image5copy = Image5.copy() 
    
        Mastercopy.paste(Image1copy, (0, 0)) 
        Mastercopy.paste(Image2copy, (365, 0)) 
        Mastercopy.paste(Image3copy, (0, 200)) 
        Mastercopy.paste(Image4copy, (365, 200))
        #Mastercopy.paste(Image5copy, (0, 400))     
        # save the image
        Mastercopy.save('C:\\DEV\\Python\\Datasets\\master.png')   

        im = Image.open('C:\\DEV\\Python\\Datasets\\master.png') 
        #im = im.resize((366, 200), Image.ANTIALIAS)
        rgb_im = im.convert('RGB')
        now = datetime.now().strftime("%Y-%m-%d")
        rgb_im.save("C:\\DEV\\Python\\Datasets\\borsa\\bugun\\" + d3[x] + "-" + now + ".jpg")

    
        # data rows of csv file 
        degisim = degisim.replace("(","").replace(")", "").replace("%","")
        if "-" in degisim:        
            rows = ['ok', d2[x], d3[x], d4[x], d5[x], d6[x], d7[x], Avgvolume, volume, price, onceki,degisim ]    
        else:
            rows = ['ok', d2[x], d3[x], d4[x], d5[x], d6[x], d7[x], Avgvolume, volume, price, onceki,'', degisim ] 
    
    
        with open(filename, 'a', newline='') as csvfile: 
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(rows)
     
    except:
        rows = ['Error', d2[x], d3[x], d4[x], d5[x], d6[x], d7[x], Avgvolume, volume, price, onceki,degisim ]   
        with open(filename, 'a', newline='') as csvfile: 
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(rows)
        print("error happaned")    
    print("loop done")
print("program done")
        