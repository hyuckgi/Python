import requests
from bs4 import BeautifulSoup



def search_daum_dict(query_keyword):

    url = """http://alldic.daum.net/search.do?q={0}"""

    r = requests.get(url.format(query_keyword))

    soup = BeautifulSoup(r.text)
    # print soup
    result_means = soup.select('.txt_search')

    for result_mean in result_means:

        print (result_mean.get_text())

if __name__ == "__main__":
    search_daum_dict("hello")
