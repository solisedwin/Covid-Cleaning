import os
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

	def format_message(self):
		number_of_stocked_products = len(self.stocked_products_urls)
		intro_message = "{num_stocked} stocked products were found on Amazon \n".format(num_stocked=number_of_stocked_products)
		links = ""
		for url in self.stocked_products_urls:
			links += url + '\n' 
		text_message = intro_message + links
		return text_message

	def send_message(self):
		client = self.create_client()
		body_message = self.format_message()
		sent_message = client.messages.create(body=body_message,from_='+xxxxxxxxxxx',to='+xxxxxxxxxxx')
		print(sent_message.sid)
