from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
from selenium.webdriver.common.by import By
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("C:/Users/Admin/Desktop/whitehat/whitehat python/pro 127/chromedriver.exe")
browser.get(START_URL)
time.sleep(10)
def scrape():
    headers = ["Proper name","Mass","Distance","Radius"]
    star_data = []
    for i in range(0,80):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for ul_tag in soup.find_all("ul", attrs={"class", "brightest_stars"}):
            li_tags = ul_tag.find_all("li")
            temp_list = []
            for index, li_tag in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
            star_data.append(temp_list)
    with open("scrape.csv","w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(star_data)
scrape()