
from re import X
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


def DataPon(stnumber):
    stpon = 650
    testnumber = stnumber.replace("%","")
    testnumber = stnumber.replace("—","0.01")
    testnumber = testnumber.replace(",", "")
    testnumber = testnumber.replace("%", "")
    print(testnumber)
    stpon = stpon + int(float(testnumber) * 3.1415) 
    return stpon

PATH = "C:\DEV\Python\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.set_window_size(1300,1000);



print("Basladi")
with open('borsastat.csv', mode='w', newline='') as borsa_file:
    borsa_writer = csv.writer(borsa_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)    
    with open('borsaoku.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0    
        for row in csv_reader:
            #time.sleep(1)
            print(row[11] + " " + row[1] + " " +  row[0])
            if (row[11] != "done"):
                line_count += 1
                linkpath = "https://www.google.com/finance/quote/" + row[1] +":" + row[0] 
                driver.get(linkpath)
                driver.implicitly_wait(10)
                wait = WebDriverWait(driver, 2)
                time.sleep(2)
                el = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/c-wiz/div/div[4]/div/div/main/div[2]/div[1]/div[1]/c-wiz/div/div[4]")))
                el.screenshot('C:\\DEV\\Python\\Datasets\\g-1d.png')
                time.sleep(1)
                btn5d = driver.find_element(By.XPATH, "/html/body/c-wiz/div/div[4]/div/div/main/div[2]/div[1]/div[1]/c-wiz/div/div[2]/div/div/div/div/div/span/button[2]/span[2]") 
                btn5d.click()
                time.sleep(1)
                el.screenshot('C:\\DEV\\Python\\Datasets\\g-5d.png')
                btn5d = driver.find_element(By.XPATH, "/html/body/c-wiz/div/div[4]/div/div/main/div[2]/div[1]/div[1]/c-wiz/div/div[2]/div/div/div/div/div/span/button[3]/span[2]") 
                btn5d.click()
                time.sleep(1)
                el.screenshot('C:\\DEV\\Python\\Datasets\\g-1m.png')
                btn5d = driver.find_element(By.XPATH, "/html/body/c-wiz/div/div[4]/div/div/main/div[2]/div[1]/div[1]/c-wiz/div/div[2]/div/div/div/div/div/span/button[4]/span[2]") 
                btn5d.click()
                time.sleep(1)
                el.screenshot('C:\\DEV\\Python\\Datasets\\g-6m.png')
          
                bilgiler =[]
                bilgiler = driver.find_elements(By.TAG_NAME, "td")
                n=0
                r=0
                o=0
                t=0
                p=0
                for bilgi in bilgiler:
                    #print(str(n) + " " + bilgi.text)
                    #print(bilgiler[n+2])
                    if bilgi.text == "Revenue":
                        r=n+2
                    if r==n:
                        Revenue = bilgi.text                                          
                    if bilgi.text == "Operating expense":
                       o=n+2                       
                    if o==n:
                        OpExpense = bilgi.text                                           
                    if bilgi.text == "Net income":
                       t=n+2                       
                       
                    if t==n:
                        NetIncome = bilgi.text                        
                                             
                    if bilgi.text == "Net profit margin":
                       p=n+2                       
                       
                    if p==n:
                        NetProfit = bilgi.text                                                          
                        
                        
                        
                    n=n+1
                #print(Revenue)
                #print(OpExpense)
                #print(NetIncome)
                #print(NetProfit)
                    

                #Revenue = driver.find_element(By.XPATH, "/html/body/c-wiz/div/div[4]/div/div/main/div[2]/div[1]/c-wiz/div/div[2]/div/div[1]/span/div/table/tr[2]/td[3]/span")
                #OpExpense = driver.find_element(By.XPATH, "/html/body/c-wiz/div/div[4]/div/div/main/div[2]/div[1]/c-wiz/div/div[2]/div/div[1]/span/div/table/tr[3]/td[3]/span")
                #NetIncome = driver.find_element(By.XPATH, "/html/body/c-wiz/div/div[4]/div/div/main/div[2]/div[1]/c-wiz/div/div[2]/div/div[1]/span/div/table/tr[4]/td[3]/span")
                #NetProfit = driver.find_element(By.XPATH, "/html/body/c-wiz/div/div[4]/div/div/main/div[2]/div[1]/c-wiz/div/div[2]/div/div[1]/span/div/table/tr[5]/td[3]/span")
                #EarningPerShare = driver.find_element(By.XPATH, "/html/body/c-wiz/div/div[4]/div/div/main/div[2]/div[1]/c-wiz/div/div[2]/div/div[1]/span/div/table/tr[6]/td[3]/span")
                #Ebitda = driver.find_element(By.XPATH, "/html/body/c-wiz/div/div[4]/div/div/main/div[2]/div[1]/c-wiz/div/div[2]/div/div[1]/span/div/table/tr[7]/td[3]/span")

                im = Image.open('C:\\DEV\\Python\\Datasets\\g-1d.png')
                im1 = im.crop((40,0,650,241))
                #im1.show()
                im1.save("C:\\DEV\\Python\\Datasets\\1d.png")
                time.sleep(1)    
                im = Image.open('C:\\DEV\\Python\\Datasets\\g-5d.png')
                im1 = im.crop((40,0,650,241))
                #im1.show()
                im1.save("C:\\DEV\\Python\\Datasets\\5d.png")
                im = Image.open('C:\\DEV\\Python\\Datasets\\g-1m.png')
                im1 = im.crop((40,0,650,241))
                #im1.show()
                im1.save("C:\\DEV\\Python\\Datasets\\1m.png")

                im = Image.open('C:\\DEV\\Python\\Datasets\\g-6m.png')
                im1 = im.crop((40,0,650,241))
                #im1.show()
                im1.save("C:\\DEV\\Python\\Datasets\\6m.png")  
    
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
    
                Mastercopy.paste(Image1copy, (0, 0)) 
                Mastercopy.paste(Image2copy, (650, 0)) 
                Mastercopy.paste(Image3copy, (0, 241)) 
                Mastercopy.paste(Image4copy, (650, 241))        
                # save the image
                Mastercopy.save('C:\\DEV\\Python\\Datasets\\master.png')   

               

                im = Image.open('C:\\DEV\\Python\\Datasets\\master.png')     
                draw = ImageDraw.Draw(im) 

                draw.line((650,500, DataPon(NetProfit),500), fill="black" ,width = 10)
                draw.line((650,515, DataPon(Revenue),515), fill="black" ,width = 10)
                draw.line((650,530, DataPon(OpExpense),530), fill="black" ,width = 10)
                draw.line((650,545, DataPon(NetIncome),545), fill="black" ,width = 10)
                #draw.line((650,560, DataPon(Ebitda.text),560), fill="black" ,width = 10)
                #im.show()
                im = im.resize((650, 300), Image.ANTIALIAS)
                im.save("C:\\DEV\\Python\\Datasets\\borsa\\bugun\\" + row[1] + ".png")
            
                borsa_writer.writerow([row[0], row[1], row[2],  Revenue, OpExpense, NetIncome])








driver.close