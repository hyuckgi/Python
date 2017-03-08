import requests
from bs4 import BeautifulSoup



def crawling(url):
    source_code = requests.get(url)

    soup = BeautifulSoup(source_code.text)
    titles = soup.select('.t_subject > a:nth-of-type(1)')
    for title in titles:

        print title.string;


crawling('http://gall.dcinside.com/board/lists/?id=baseball_new4')
