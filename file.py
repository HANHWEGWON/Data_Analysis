import requests
from bs4 import BeautifulSoup

x = input("제목을 입력하세요.")
print("\n--------------------------")


for page in range(1, 32, 10):
    print("----------------------------------------------")
    url = f"https://search.naver.com/search.naver?where=news&sm=tab_pge&query={x}&start={page}"
    response = requests.get(url)
    text = response.text
    soup = BeautifulSoup(text, 'html.parser')
    choice = soup.select('.news_tit')

    for z in choice:
        print(z['title'])
        print(z['href']+"\n")

