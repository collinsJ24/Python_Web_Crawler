# Import libraries
import requests
from urllib.request import Request, urlopen
import time
from bs4 import BeautifulSoup
from lxml import etree
from lxml import html

# Set the URL you want to webscrape from
url = 'https://www.myucd.ie/courses/a-z-course-list/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

response = requests.get(url, headers=headers).content

count = 1 
while count < 500:
       tree=html.fromstring(response)
       hyperlink = tree.xpath('//*[@id="all"]/div[1]/div[1]/div/ul/li[' + str(count) + ']/a/@href')
       for i in hyperlink:
        print(i)
        CoursePage = requests.get(i, headers=headers).content
        tree2=html.fromstring(CoursePage)
        CourseCode = tree2.xpath('/html/body/section[1]/div/div/div[1]/div[1]/div[2]/div[1]/p[3]/text()[2]')
        print(CourseCode)
       count += 1