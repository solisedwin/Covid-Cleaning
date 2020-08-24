from lxml import html
from bs4  import BeautifulSoup as bs
import requests
class WebParser(object):

    def __init__(self):
       self.stocked_product_links = []

    def connect_to_site(self,link,proxy,header):
        page = requests.get(link,proxies={"http": proxy,"http":proxy},headers=header)
        soup = bs(page.content,"html.parser")
        return soup

    def item_stock_status(self,soup,link):
        is_in_stock = soup.find('span', class_='a-size-medium a-color-success')
        if is_in_stock:
            print('~~~ Item is in stock!!')
            self.stocked_product_links.append(link)
        else:
            print(':( not in stock' )







