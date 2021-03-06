import json
from .config import token_path
import os
from .logger import Logger

class Token_Manager:

	def __init__(self):
		self.token_path = os.path.join(os.path.expanduser("~"), token_path)
		if not os.path.exists(self.token_path):
			os.makedirs(self.token_path)

		self.token_file_name = "token.json"
		self.logger = Logger()

	def save_token(self, token):

		token_data = {}
		token_data["token"] = token
		token_file_path = os.path.join(self.token_path, self.token_file_name)
		token_file = open(token_file_path, "w")
		token_file.write(json.dumps(token_data))
		token_file.close()

		return 1

	def get_token(self):

		token_file_path = os.path.join(self.token_path, self.token_file_name)
		
		if not os.path.exists(token_file_path):
			self.logger.fail("You are not logged in. Please log in first.")
			return 0

		token_file = open(token_file_path)
		token = json.loads(token_file.read())
		if not token or token == "" or not token.get("token") or token.get("token") == "":
			return 0

		token = token.get("token")
		
		return token
