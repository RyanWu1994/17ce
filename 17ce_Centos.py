#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Get_17CE_version 1.2.0

from sqlalchemy import create_engine
from collections import Counter
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import os
import random
import time
import pandas as pd


# In[ ]:


def SeleniumGetPhoto(URL):
    
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('blink-settings=imagesEnabled=false')
    options.add_argument('--enable-features=OverlayScrollbar')

    chromedriver = '/root/chromedriver'
    driver = webdriver.Chrome(executable_path=chromedriver, options=options)
    driver.get("https://www.17ce.com/")
    time.sleep(3)
    driver.find_element(By.ID, "nav1").click()
    driver.find_element(By.ID, "url").click()
    driver.find_element(By.ID, "url").send_keys(URL)
    driver.find_element(By.ID, "su").click()
    web = URL.replace("https://","").replace("/","")
    time.sleep(60)
    soup = BeautifulSoup(driver.page_source,"html.parser")
    driver.close()
    Date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return web , soup, Date

#----------------------------------------------------------------------------

def Getmain(web,soup,Date):
    
    main_result = []

    table = soup.find("tbody")

    for i in table.find_all("tr"):
        
        line = i.find_all("td")[0].text
        
        try:
            fastestnode = i.find_all("td")[1].find("font",class_="fl").text
        except:
            fastestnode = "-"

        try:
            fastestsec = i.find_all("td")[1].find("font",class_="fr").text
        except:
            fastestsec = "-"

        try:
            slowestnode = i.find_all("td")[2].find("font",class_="fl").text
        except:
            slowestnode = "-"

        try:
            slowestsec = i.find_all("td")[2].find("font",class_="fr").text
        except:
            slowestsec = "-"

        try:
            average = i.find_all("td")[3].find("font",class_="fr").text
        except:
            average = "-"

        result_dict = {
                "URL":web,
                "Date":Date,
                "Line":line,
                "Fastest_node":fastestnode,
                "Fastest_node_seconds":fastestsec,
                "Slowest_node":slowestnode,
                "Slowest_node_seconds":slowestsec,
                "Average_response":average
            }

        main_result.append(result_dict)
    
    return main_result


#----------------------------------------------------------------------------

def Getnode(web,soup,Date):
    node_list = []
    node_table = soup.find("table",{"id":"tblSort"})
    table_tr = node_table.find_all("tr")

    count = 0

    for tr in table_tr[2:]:
        count += 1

        for number,content in enumerate(tr):

            if content.text == "":
                continue

            else:

                if number == 0:
                    Node = content.text

                elif number == 1:
                    ISP = content.text

                elif number == 2:
                    Province = content.text

                elif number == 3:
                    IP = content.text

                elif number == 4:
                    DNS_position = content.text

                elif number == 5:
                    Ststus = content.text

                elif number == 6:
                    Total_time = content.text

                elif number == 7:
                    Resolution_time = content.text

                elif number == 8:
                    Connection_time = content.text

                elif number == 9:
                    Download_time = content.text

                elif number == 10:
                    First_byte_time = content.text

                elif number == 11:
                    File_size = content.text

                elif number == 12:
                    Download_size = content.text

                elif number == 13:
                    Download_speed = content.text

        node_dict = {
            "URL" : web,
            "Date" : time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            "Node" : Node,
            "ISP" : ISP,
            "Province" : Province,
            "IP" : IP,
            "DNS_position" : DNS_position,
            "Ststus" : Ststus,
            "Total_time" : Total_time,
            "Resolution_time" : Resolution_time,
            "Connection_time" : Connection_time,
            "Download_time" : Download_time,
            "First_byte_time" : First_byte_time,
            "File_size" : File_size,
            "Download_size" : Download_size,
            "Download_speed" : Download_speed

        }

        node_list.append(node_dict)
        
    return node_list

#----------------------------------------------------------------------------

#連結資料庫
#範本解釋:create_engine('mysql+mysql_driver://mysql帳號:mysql密碼@機器ip:mysql_port/DB名稱?其他參數', encoding='mysql編碼'
#charset=utf8 資料庫編碼

def List_to_mysql(user,passwd,ip,db_name,table_name,result_list):

    engine = create_engine('mysql+mysqlconnector://'+ user +':'+ passwd +'@'+ip+'/'+ db_name +'?charset=utf8', encoding='utf-8')
    con = engine.connect() #建立連結
    
    for item in result_list:
        df = pd.DataFrame(item, index=[0])
        try:
            df.to_sql(name=table_name,con=con,if_exists='append',index=False) #假設table已存在 就自動往下加入data

        except Exception as e:
            if 'PRIMARY' in str(e):
                pass

    con.close() 
    engine.dispose()

#----------------------------------------------------------------------------

# Run code

URL_list = ["https://smtv.raccoontv.com/"]

for URL in URL_list:
    web , soup , Date = SeleniumGetPhoto(URL)
    main_result = Getmain(web,soup,Date)
    node_result = Getnode(web,soup,Date)

    user = "root"
    passwd = "Pn123456"
    ip = "192.168.22.110:3306"
    db_name = "17CE"
    
    List_to_mysql(user=user,passwd=passwd,ip=ip,db_name=db_name,table_name="main_information",result_list=main_result)
    print(URL ," - main_result -"," insert mysql...done")
    
    List_to_mysql(user=user,passwd=passwd,ip=ip,db_name=db_name,table_name="node_information",result_list=node_result)
    print(URL ," - node_result -"," insert mysql...done") 
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




