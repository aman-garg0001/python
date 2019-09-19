import requests
from bs4 import BeautifulSoup
url = "https://codeforces.com/profile/"
handle = input("Enetr your handle:  ")
url += handle
try:
    page = requests.get(url)
    
    soup = BeautifulSoup(page.text,'html5lib')
    path = soup.find("div",{"class":"user-rank"})
    # info = soup.find("div",{"class":"info"})
    # ul = info.find("ul")
    # li = ul.find("li")
    # rat = li.find("span")
    rat = soup.select("div.info li span")
    
    print(path.text)
    print(rat[0].text,rat[1].text)
except:
    print("Error : pls check internet or User-handle")
    
input() #to pause console