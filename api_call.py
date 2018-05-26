import json
import requests
from config import *

def APi_call:
	def __init__(self):
		self.API_BASE_URL = API_BASE_URL
		self.requestPayload = {}
		self.headers = {}

	def apicall(self, payload, headers):
		self.headers["Content-Type"] = "application/json"

		if headers.get("Authorization"):
			self.headers["Authorization"] = headers.get("Authorization")

		resp = requests.request("POST", url, data=json.dumps(requestPayload), headers=headers)

		return resp.json()
