from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
url='https://coinmarketcap.com/'
driver=webdriver.Chrome()
driver.get(url)
nameclass='cmc-link'
name=driver.find_elements(By.CLASS_NAME,nameclass)
num=[j for j in range(1,12)]
j=0
for i in name:
    namexpath=f'//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[4]/table/tbody/tr[{num[j]}]/td[3]/div/a/div/div/p'
    cname=i.find_element(By.XPATH,namexpath).text
    print(cname)
    j+=1

