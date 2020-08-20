from lxml import html
from bs4  import BeautifulSoup as bs
import requests
class WebParser(object):

    def __init__(self):
        self.stocked_products_links = []

    def connect_to_site(self,link,proxy,header):
            try:
                print('Link: ' + str(link))
                page = requests.get(link,proxies={"http": proxy, "http": proxy},headers=header)
                soup = bs(page.content, 'lxml')
                print(soup.prettify())
            except requests.exceptions.RequestException as e:
                print('Error connect to sites {link}, Error is: {error}'.format(link=link,error=e))

