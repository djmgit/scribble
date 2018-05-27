from statuses import *
import getpass
from api_call import Api_call

class Login:
	def __init__(self):
		self.username = ""
		self.password = ""
		self.path = "login"

	def get_cred(self):
		username = input("Enter username : ")
		password = getpass.getpass(prompt="Enter password : ")

		self.username = username
		self.password = password
		self.repassword = retype_password

	def login(self):
		headers = {}
		payload = {}

		payload['username'] = self.username
		payload['password'] = self.password

		print ("Logging you in...")

		resp = Api_call().apicall(payload, headers, self.path)
		if resp.get("status") == USERNAME_NOT_FOUND:
			print ("Please enter an username")
			return 0

		if resp.get("status") == PASSWORD_NOT_FOUND:
			print ("Please provide a password")
			return 0

		if resp.get("status") == ERROR:
			data = resp.get("data")
			code = data.get("code")
			message = data.get("message")
			print ("{} : {}".format(code, message))
			return 0

		if resp.get("status") == OK:
			print ("You have been successfuly logged in")

			data = resp.get("data")
			auth_token = data.get("auth_token")

			return 1
