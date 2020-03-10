import requests
from bs4 import BeautifulSoup
from time import sleep

url = "http://static.cricinfo.com/rss/livescores.xml"
while True:
    r = requests.get(url)
    while r.status_code is not 200:
        r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    data = soup.find_all('description')
    # print(data)
    for i in data:
        if "India" in str(i.text):
            socre = i.text
            print(socre)
            break
    sleep(3600)
