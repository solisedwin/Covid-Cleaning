import os
import requests
from twilio.rest import Client

class PhoneMessage(object):
	def __init__(self, stocked_products_urls):
		super(PhoneMessage, self).__init__()
		self.stocked_products_urls = stocked_products_urls

	def create_client(self):
		account_sid = os.environ['TWILIO_ACCOUNT_SID']
		auth_token = os.environ['TWILIO_AUTH_TOKEN']
		client = Client(account_sid, auth_token)
		return client

	def shorten_urls(self):
		shortned_urls = []
		for url in self.stocked_products_urls:
			res = requests.post('https://api.short.cm/links', {
		  	'domain': 'solisedwin10.shortcm.li',
		  	'originalURL': '{url}'.format(url=url),
			}, headers = {
		  	'authorization': os.environ['SHORTIO_SECRET_KEY']
			}, json=True)

			res.raise_for_status()
			data = res.json()
			shortned_urls.append(data['secureShortURL'])
		return shortned_urls

	def format_message(self):
		message_urls = self.shorten_urls()
		number_of_stocked_products = len(self.stocked_products_urls)
		intro_message = "{num_stocked} stocked products were found on Amazon \n".format(num_stocked=number_of_stocked_products)
		body_message =  '\n'.join(message_urls)
		text_message = intro_message + body_message
		return text_message

	def send_message(self):
		client = self.create_client()
		sms_message = self.format_message()
		sent_message = client.messages.create(body=sms_message,from_='+xxxxxxxxxxxxxx',to='+xxxxxxxxxxxxxxxx')
		print(sent_message.sid)
