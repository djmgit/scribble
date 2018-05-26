import json
import requests
from config import *

class Api_call:
	def __init__(self):
		self.API_BASE_URL = API_BASE_URL
		self.requestPayload = {}
		self.headers = {}

	def apicall(self, payload, headers, path):
		self.headers["Content-Type"] = "application/json"

		if headers.get("Authorization"):
			self.headers["Authorization"] = headers.get("Authorization")

		resp = requests.request("POST", self.API_BASE_URL + '/' + path, data=json.dumps(payload), headers=headers)

		return resp.json()
