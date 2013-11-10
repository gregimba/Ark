import requests
from time import sleep


class Ark(object):
	"""This is a python wrapper for the ARK api"""
	def __init__(self,api_token):
		self.api_token = api_token
		self.header = {'api_token' : self.api_token }
	
	def check_token(self,full_object=False):
		"""Checks the number of calls your token has left"""
		base_url = "https://testapi.ark.com"
		url = base_url + "/token_request" 
		request = requests.get(url,headers=self.header)
		
		while request.status_code == 302:
			sleep(1)
			request = requests.get(url,headers=self.header)		

		if request.status_code != 200:
			return request.status_code

		if full_object:
			return request
		else:
			return request.json()['left']

	def email(self, email, full_object=False):
		"""Fetches a user profile via email"""
		base_url = "https://testapi.ark.com/email/"
		url = base_url + email
		request = requests.get(url,headers=self.header)
		
		while request.status_code == 302:
			sleep(1)
			request = requests.get(url,headers=self.header)		

		if request.status_code != 200:
			return request.status_code
		
		if full_object:
			return request
		else:
			return request.json()

	def twitter(self, handle, full_object=False):
		"""Fetches a user profile via twitter handle"""
		base_url = "https://testapi.ark.com/network/tw:"
		url = base_url + handle
		request = requests.get(url,headers=self.header)
		
		while request.status_code == 302:
			sleep(1)
			request = requests.get(url,headers=self.header)		

		if request.status_code != 200:
			return request.status_code

		if full_object:
			return request
		else:
			return request.json()

	def facebook(self, facebook_url, full_object=False):
		"""Fetches user profile via facebook url"""
		base_url = "https://testapi.ark.com/network/fb:"
		url = base_url + facebook_url
		request = requests.get(url,headers=self.header)
		
		while request.status_code == 302:
			sleep(1)
			request = requests.get(url,headers=self.header)		

		if request.status_code != 200:
			return request.status_code
		
		if full_object:
			return request
		else:
			return request.json()