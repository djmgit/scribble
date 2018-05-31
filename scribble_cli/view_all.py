from statuses import *
import getpass
from api_call import Api_call
from token_manager import Token_Manager
from tabulate import tabulate

class View_all:

	def __init__(self):
		self.token = ""
		self.path = "all_notes"

	def set_params(self):
		token = Token_Manager().get_token()
		if token == 0:
			exit()

		self.token = token

	def view_all(self):
		headers = {}
		payload = {}

		headers["Authorization"] = self.token

		print ("Retrieving your notes...")

		resp = Api_call().apicall(payload, headers, self.path)

		if resp.get("status") == TOKEN_NOT_FOUND or resp.get("status") == NOT_LOGGED_IN :
			print ("You are not logged in. Please log in first.")
			print ("hehe")
			return 0

		if resp.get("status") == ERROR:
			data = resp.get("data")
			code = data.get("code")
			message = data.get("message")
			print ("{} : {}".format(code, message))
			return 0

		data = resp.get("data")

		if len(data) == 0:
			print ("You have not created any notes yet!")
			exit()

		table = []
		table_headers = ["Note id", "Note"]
		for note in data:
			table.append([note["note_id"], note["note_title"]])

		print ("\n")
		print (tabulate(table, table_headers, tablefmt="orgtbl"))
		print ("\n")

		return 1
