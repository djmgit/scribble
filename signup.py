from config import *
from statuses import *
import getpass

class Signup:
	def __init__(self):
		self.API_BASE_URL = API_BASE_URL

	def get_cred(self):
		username = raw_input("Enter username")
		password = getpass.getpass(prompt="Enter password")

		self.username = username
		self.password = password

	def signup():

