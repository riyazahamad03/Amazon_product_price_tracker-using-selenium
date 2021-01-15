from selenium import webdriver
import requests


ASIN=input("Please Enter Asin of product : ")
Desired_Price=int(input("please enter the desired price ,Which Should Be In The Format Of Less Than < :"))
print("Thank You I Will Be Notifying You Once When The Price Drops ")
url='https://www.amazon.in/dp/'+ASIN
url_1='https://www.amazon.in/gp/offer-listing/'+ASIN

webdriver_path =r"Your Webdriver Path"
options = webdriver.ChromeOptions()
#options.add_argument('--headless') 
options.add_argument('start-maximized') 
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')
options.add_argument('--disable-popup-blocking')
driver=webdriver.Chrome(webdriver_path,options=options)

def check_price():
    
    try:
        driver.get(url)
        name = driver.find_element_by_id("productTitle").text
        price=driver.find_element_by_id("priceblock_ourprice").text
        converted_price=float(price.replace("₹","").replace(",","").replace(" ",""))
        if(converted_price <= Desired_Price ):
            send_message("\n" "\n"+"Good News!! Price Fell Down"+"\n" "\n"+name+"\n" "\n"+price+ "\n" "\n"+ url)
        print(name)
        print(converted_price)
    except:
        print("*price unavaivable")
        
    try:
        driver.get(url_1)
        name_1=driver.find_element_by_css_selector("#olpProductDetails > h1").text
        price_1=driver.find_element_by_css_selector("#olpOfferList > div > div > div:nth-child(3) > div.a-column.a-span2.olpPriceColumn > span > span").text
        converted_price_1 = float(price_1.replace(" ","").replace(",",""))
        if (converted_price_1 <= Desired_Price):
            send_message("\n" "\n"+"Good News!! Price Fell Down"+"\n" "\n"+name_1+"\n" "\n"+price_1+ "\n" "\n"+ url_1)

            print(name_1)
            print(converted_price_1)
    except:
        print("price unavaivable")

def send_message(bot_message):
    
    bot_token = 'Your Bot Token'
    bot_chatID = 'Your Bot Chat ID'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()

while(True):
    check_price()
    time.sleep(4)
    