from statuses import *
import getpass
from api_call import Api_call
from token_manager import Token_Manager
from tabulate import tabulate

class Search:

	def __init__(self):
		self.token = ""
		self.path = "note_search"
		self.search_data = ""
		self.fields = ""
		self.body_length = 72

	def set_params(self, search_data, fields=None):
		token = Token_Manager().get_token()
		if token == 0:
			exit()

		self.token = token
		self.search_data = search_data
		self.fields = fields

	def search(self):
		headers = {}
		payload = {}

		headers["Authorization"] = self.token

		payload["search"] = self.search_data
		if self.fields:
			payload["fields"] = self.fields

		print ("Searching...")

		resp = Api_call().apicall(payload, headers, self.path)

		if resp.get("status") == TOKEN_NOT_FOUND or resp.get("status") == NOT_LOGGED_IN :
			print ("You are not logged in. Please log in first.")
			return 0

		if resp.get("status") == SEARCH_DATA_NOT_FOUND:
			print ("Please mention search data")
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

		data = resp.get("data")
		if len(data) == 0:
			print ("NO matching data found!")
			return 1

		table = []
		table_headers = ["Note Id", "Note Tile", "Note Body", "Keywords", "Category"]

		for note in data:
			table.append([note["note_id"], note["note_title"], note["note_body"], note["keywords"], note["category"]])

		print ("\n")
		print (tabulate(table, table_headers, tablefmt="orgtbl"))
		print ("\n")

		return 1

		
