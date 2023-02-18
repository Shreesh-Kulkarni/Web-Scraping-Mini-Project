from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
url='https://coinmarketcap.com/'
driver=webdriver.Chrome()
driver.get(url)
nameclass='cmc-link'
name=driver.find_elements(By.CLASS_NAME,nameclass)
num=[j for j in range(1,11)]
k=0
d={}
try:
    for i in name:
        value=[]
        namexpath=f'//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[4]/table/tbody/tr[{num[k]}]/td[3]/div/a/div/div/p'
        pricexpath=f'//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[4]/table/tbody/tr[{num[k]}]/td[4]/div/a'
        cname=i.find_element(By.XPATH,namexpath).text
        cprice=i.find_element(By.XPATH,pricexpath).text
        value.append(cprice)
        d[cname]=value
        k+=1
except IndexError:
    print(d)



