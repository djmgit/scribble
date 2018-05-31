from .statuses import *
import getpass
from .api_call import Api_call
from .token_manager import Token_Manager

class Note:

	def __init__(self):
		self.token = ""
		self.note_title = ""
		self.note_body = ""
		self.keywords = ""
		self.category = ""
		self.path = "add_note"

	def set_params(self, note_title, note_body, keywords, category):
		self.note_title = note_title
		self.note_body = note_body
		self.keywords = keywords
		self.category = category

		token = Token_Manager().get_token()
		if token == 0:
			exit()

		self.token = token

	def save_note(self):
		headers = {}
		payload = {}

		headers["Authorization"] = self.token

		payload["note_title"] = self.note_title
		payload["note_body"] = self.note_body
		payload["keywords"] = self.keywords
		payload["category"] = self.category

		print ("saving your note...")

		resp = Api_call().apicall(payload, headers, self.path)

		if resp.get("status") == TOKEN_NOT_FOUND or resp.get("status") == NOT_LOGGED_IN :
			print ("You are not logged in. Please log in first.")
			return 0

		if resp.get("status") == NOTE_TITLE_NOT_FOUND:
			print ("Please spicify a title for your note.")
			return 0

		if resp.get("status") == NOTE_BODY_NOT_FOUND:
			print ("Body of the note cannot be empty.")
			return 0

		if resp.get("status") == ERROR:
			data = resp.get("data")
			code = data.get("code")
			message = data.get("message")
			print ("{} : {}".format(code, message))
			return 0

		if resp.get("status") == OK:
			print ("Your note has been save successfully!")
			return 1

		return 0