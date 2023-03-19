from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
def scrape_data(c):
    url='https://coinmarketcap.com/?page=1'
    driver=webdriver.Chrome()
    driver.get(url)
    time.sleep(20)
    nameclass='cmc-link'
    name=driver.find_elements(By.CLASS_NAME,nameclass)
    num=[j for j in range(1,c+1)]
    k=0
    d=[]
    try:
        for i in name:
                value=[]
                namexpath=f'//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[4]/table/tbody/tr[{num[k]}]/td[3]/div/a/div/div/p'
                pricexpath=f'//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[4]/table/tbody/tr[{num[k]}]/td[4]/div/a'
                #hourchangexpath=f'//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[4]/table/tbody/tr[{num[k]}]/td[6]/span'
                mcapxpath=f'//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[4]/table/tbody/tr[{num[k]}]/td[8]/p'
                volxpath=f'//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[4]/table/tbody/tr[{num[k]}]/td[9]/div/a/p'
                circxpath=f'//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[4]/table/tbody/tr[{num[k]}]/td[10]/div/div[1]/p'
                cname=i.find_element(By.XPATH,namexpath).text
                cprice=i.find_element(By.XPATH,pricexpath).text
                mcap=i.find_element(By.XPATH,mcapxpath).text
                vol=i.find_element(By.XPATH,volxpath).text
                circ=i.find_element(By.XPATH,circxpath).text
                #hchange=i.find_element(By.XPATH,hourchangexpath)

                #hchange=i.find_element(By.XPATH,hourchangexpath).text
                value.extend([cname,cprice,mcap,vol,circ])
                d.append(value)
                k+=1
    except IndexError:
        pass
    df = pd.DataFrame(d, columns=['Name', 'Price', 'Market Cap', 'Volume', 'Circulating Supply'])
    return df


#