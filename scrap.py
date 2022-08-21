from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import *
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
import csv
# url = 'https://www.youtube.com/c/ChicoCrypto/videos?view=0&sort=dd&shelf_id=0'
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# # driver = webdriver.Chrome()
# driver.get(url)
# # style-scope ytd-grid-video-renderer
# # //*[@id="video-title"]
# # //*[@id="metadata-line"]/span[1]
# # print("xxxxxxxxeeeeeeeeeeeeeeeeeeeexxxxxxxxxxxxxx")

# videos = driver.find_elements(By.TAG_NAME, 'ytd-grid-video-renderer')
# # print("xxxxxxxxeeeeeeeeeeeeeeeeeeeexxxxxxxxxxxxxx")

# for i in videos:
#     # print("xxxxxxxxeeeeeeeeeeeeeeeeeeeexxxxxxxxxxxxxx")
#     title = i.find_element(By.XPATH, './/*[@id="video-title"]').text
#     views = i.find_element(By.XPATH,'.//*[@id="metadata-line"]/span[1]').text
#     print(title, " video having views ", views)

url = 'https://cointelegraph.com/tags/bitcoin'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)
titles = []
dates = []
lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
wl=1
while(wl):
    wl-=1
    try:
        # WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, 'posts-listing__more-btn'))).click()
        # page = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'posts-listing__more-btn')))
        l = driver.find_element(By.CLASS_NAME,'posts-listing__more-btn')
        l.click()
        lenofpage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        art =  driver.find_elements(By.CLASS_NAME, 'post-card-inline')
        for i in art:
            title = i.find_element(By.CLASS_NAME, 'post-card-inline__title').text
            date  = i.find_element(By.CLASS_NAME, 'post-card-inline__date').text
            titles.append(str(title))
            dates.append(str(date))
            print(title," line 47")
        time.sleep(5)
    except TimeoutException:
        print("NOOOOOOOOOOOOOOOOT      FOUND      ELEMENT  ")
        break

# df = pd.DataFrame({'Titles': titles, 'Date': date})
# writer = pd.ExcelWriter('pandas_simple.xlsx')
# df.to_excel(writer,'Sheet1')
# writer.save()
# with open('/','wb') as csvFile: #EDIT - because comment.
#     writer = csv.writer(csvFile)
#     # writer.writerows(csvstff)
info = { 
        'Titles': titles, 
        'Date': date 
        }
key = ["Titles", "Date"]
with open('a.csv','w') as f:
    write = csv.writer(f)
    write.writerows(titles)
    # dict_writer = csv.DictWriter(f,key)
    # dict_writer.writeheader()
    # dict_writer.writerows(info)
