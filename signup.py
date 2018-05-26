from statuses import *
import getpass
from api_call import Api_call

class Signup:
	def __init__(self):
		self.username = ""
		self.password = ""
		self.repassword = ""
		self.path = "signup"

	def get_cred(self):
		username = input("Enter username")
		password = getpass.getpass(prompt="Enter password")
		retype_password = getpass.getpass(prompt="Retype password")

		self.username = username
		self.password = password
		self.repassword = retype_password

	def signup(self):
		headers = {}
		payload = {}

		if self.password != self.repassword:
			print ("Passwords do not match!. Please try again.")
			return 0

		payload['username'] = self.username
		payload['password'] = self.password

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
			print ("{} : {}").format(code, message)
			return 0

		if resp.get("status") == OK:
			print ("You have been registered succesfully. Please login to enjoy scribble")
			return 1
