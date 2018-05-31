import json
import requests
from .config import API_BASE_URL

class Api_call:
	def __init__(self):
		self.API_BASE_URL = API_BASE_URL
		self.requestPayload = {}
		self.headers = {}

	def apicall(self, payload, headers, path):
		self.headers["Content-Type"] = "application/json"
		json_data = ""

		if headers.get("Authorization"):
			self.headers["Authorization"] = headers.get("Authorization")

		'''
		this is a hack. This application uses free version of hasura. The cluster sleeps
		when not in use for a long time. So if cluster is sleeping, then the api will fail.
		As a result an exception will be raised (as python will not able to extract any json)
		and finally the script will be terminated
		'''

		try:
			resp = requests.request("POST", self.API_BASE_URL + '/' + path, data=json.dumps(payload), headers=self.headers)
			json_data = resp.json()
		except:
			print ("Scribble is sleeping!")
			print ("Formally speaking, the hasura cluster is sleeping due to inactivity, please wake it up :P")
			exit()

		return json_data
