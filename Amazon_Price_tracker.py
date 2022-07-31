from selenium import webdriver
import requests
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from datetime import datetime
from webdriver_manager.chrome import ChromeDriverManager
import time


url=input("Please enter the your custom link : ")
#ASIN=input("Please Enter Asin of product : ")
Desired_Price=int(input("please enter the desired price ,Which Should Be In The Format Of Less Than < :"))
print("Thank You I Will Be Notifying You Once When The Price Drops ")
#url='https://www.amazon.in/dp/'+ASIN
#url_1='https://www.amazon.in/gp/offer-listing/'+ASIN

webdriver_path =r"C:\Users\riyaz\Desktop\python_scripts\chromedriver.exe"
service_obj = Service(webdriver_path)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
# options.add_argument('--headless') 
options.add_argument('start-maximized') 
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')
options.add_argument('--disable-popup-blocking')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver = webdriver.Chrome(service=service_obj)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

def check_price():
    try:
        driver.get(url)
        time.sleep(5)
        name = driver.find_element(By.ID,"productTitle").text
        try:
            price=driver.find_element(By.CSS_SELECTOR,"#corePrice_desktop > div > table > tbody > tr:nth-child(2) > td.a-span12 > span.a-price.a-text-price.a-size-medium.apexPriceToPay").text
            # print(price)
        except:
            price=driver.find_element(By.CLASS_NAME,"a-price-whole").text
            # print(price)
        converted_price=float(price.replace("₹","").replace(",","").replace(" ",""))
        if(converted_price <= Desired_Price ):
            send_message("\n" "\n"+name+"\n" "\n"+price+ "\n" "\n"+ url)
            print(name)
            print(converted_price)
            # time.sleep(60)
        else:
            print(name)
            #print(price)
            print("The Required Limit Not Reached ")
    
    except:
        print("*Price Unavaivable or not at your desired limit ")

def send_message(bot_message):
    
    bot_token = 'Your Bot Token'
    bot_chatID = 'Your Bot Chat ID'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()

while(True):
    check_price()
    time.sleep(4)
    
