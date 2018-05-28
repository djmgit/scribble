from statuses import *
import getpass
from api_call import Api_call
from token_manager import Token_Manager
from tabulate import tabulate

class Delete:

	def __init__(self):
		self.token = ""
		self.path = "delete_note"
		self.note_id = ""

	def set_params(self, note_id):
		token = Token_Manager().get_token()
		if token == 0:
			exit()

		self.token = token
		self.note_id = note_id

	def delete(self):
		headers = {}
		payload = {}

		headers["Authorization"] = self.token

		payload["note_id"] = self.note_id

		print ("Deleting your note...")

		resp = Api_call().apicall(payload, headers, self.path)

		if resp.get("status") == TOKEN_NOT_FOUND or resp.get("status") == NOT_LOGGED_IN :
			print ("You are not logged in. Please log in first.")
			return 0

		if resp.get("status") == NOTE_ID_NOT_FOUND:
			print ("Please mention a note id")
			return 0

		if resp.get("status") == DATA_NOT_FOUND:
			print ("No matching data found!")
			return 1

		if resp.get("status") == ERROR:
			data = resp.get("data")
			code = data.get("code")
			message = data.get("message")
			print ("{} : {}".format(code, message))
			return 0

		if resp.get("status") == OK:
			print ("Note has been deleted successfully!")
			return 1
		
		return 0
