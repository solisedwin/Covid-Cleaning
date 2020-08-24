import json
from bot import Bot
from parser import WebParser
import sys
from message import PhoneMessage

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

    stocked_products_urls = bot.webparser.stocked_product_links
    #Couldnt find any products that were in stock
    if not stocked_products_urls:
        sys.exit(1)
    else:
        phone_message = PhoneMessage(stocked_products_urls)
        phone_message.send_message()