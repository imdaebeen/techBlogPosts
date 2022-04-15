import requests
from bs4 import BeautifulSoup

def getPosts():
    url = "https://techblog.woowahan.com"
    res = requests.get(url)
    soup = BeautifulSoup(res.content,'html.parser')
    title = soup.find('title')
    return title.get_text()