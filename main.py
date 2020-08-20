
import json
from bot import Bot
from parser import WebParser

def get_amazon_links():
    with open('data/links.json') as links_file:
        json_links = json.load(links_file)
        wipe_products_links = json_links['Wipes']
        spray_products_links = json_links['Spray']
        return wipe_products_links, spray_products_links

if __name__ == "__main__":
    wipe_products_links,spray_products_links = get_amazon_links()
    web_parser = WebParser()
    bot = Bot(web_parser)
    bot.start_scrapying_process(wipe_products_links)
    bot.start_scrapying_process(spray_products_links)

