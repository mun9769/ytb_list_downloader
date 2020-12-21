import requests
from bs4 import BeautifulSoup

headers = {"User-Agents":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}


url = "https://www.youtube.com/playlist?list=PLdEdazAwz5Q_n47tqf0QY94ASCmWqeGX1"
res = requests.get(url,headers= headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

with open("soup_prettify.html","w",encoding="utf-8") as f:
    # f.write(res.text)
    # f.write(res.text)
    f.write(soup.prettify())