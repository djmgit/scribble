from .statuses import *
import getpass
from .api_call import Api_call
from .token_manager import Token_Manager
from .logger import Logger

class Login:
	def __init__(self):
		self.username = ""
		self.password = ""
		self.path = "login"
		self.logger = Logger()

	def get_cred(self):
		username = input("Enter username : ")
		password = getpass.getpass(prompt="Enter password : ")

		self.username = username
		self.password = password

	def login(self):
		headers = {}
		payload = {}

		payload['username'] = self.username
		payload['password'] = self.password

		print ("Logging you in...")

		resp = Api_call().apicall(payload, headers, self.path)
		if resp.get("status") == USERNAME_NOT_FOUND:
			self.logger.fail("Please enter an username")
			return 0

		if resp.get("status") == PASSWORD_NOT_FOUND:
			self.logger.fail("Please provide a password")
			return 0

		if resp.get("status") == ERROR:
			data = resp.get("data")
			code = data.get("code")
			message = data.get("message")
			self.logger.fail("{} : {}".format(code, message))
			return 0

		if resp.get("status") == OK:
			data = resp.get("data")
			auth_token = data.get("auth_token")

			r = Token_Manager().save_token(auth_token)

			self.logger.success("You have been successfuly logged in")
			return 1

		return 0


