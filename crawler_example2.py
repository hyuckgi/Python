import requests
from bs4 import BeautifulSoup



def crawling(url):
    source_code = requests.get(url)

    soup = BeautifulSoup(source_code.text)
    titles = soup.select('.now_price > span')

    for title in titles:
        print title.string;


crawling('http://www.ticketmonster.co.kr/deal/517341114?utm=TODAYSHOT&loc=1')
