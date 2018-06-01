from .statuses import *
import getpass
from .api_call import Api_call
from .token_manager import Token_Manager
from tabulate import tabulate
from .logger import Logger

class View_by_id:

	def __init__(self):
		self.token = ""
		self.path = "note_by_id"
		self.note_id = ""
		self.logger = Logger()

	def set_params(self, note_id):
		token = Token_Manager().get_token()
		if token == 0:
			exit()

		self.token = token
		self.note_id = note_id

	def view_by_id(self):
		headers = {}
		payload = {}

		headers["Authorization"] = self.token

		payload["note_id"] = self.note_id

		print ("Retrieving your note...")

		resp = Api_call().apicall(payload, headers, self.path)

		if resp.get("status") == TOKEN_NOT_FOUND or resp.get("status") == NOT_LOGGED_IN :
			self.logger.fail("You are not logged in. Please log in first.")
			return 0

		if resp.get("status") == NOTE_ID_NOT_FOUND:
			self.logger.fail("Please mention a note id")
			return 0

		if resp.get("status") == ERROR:
			data = resp.get("data")
			code = data.get("code")
			message = data.get("message")
			self.logger.fail("{} : {}".format(code, message))
			return 0

		data = resp.get("data")

		if len(data) == 0:
			self.logger.info("No note with id {} not found!".format(self.note_id))
			exit()
		
		data = data[0]
		print ("\n")
		print ("#{} {}".format(data["note_id"], data["note_title"]))
		print ("====================================================================")
		print ("\n")
		print (data["note_body"])
		print ("\n")
		if data.get("keywords") and data.get("keywords") != "":
			print ("Keywords : {}".format(data["keywords"]))
			print ("\n")
		if data.get("category") and data.get("category") != "":
			print ("category : {}".format(data["category"]))
			print ("\n")

		return 1
