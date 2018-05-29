import optparse
import sys
import editor
from signup import Signup
from login import Login
from view_all import View_all
from view_by_id import View_by_id
from note import Note
from search import Search
from delete import Delete

ACTIONS = ["register", "login", "note", "view", "search", "delete"]

def parse_and_execute_signup():
	obj = Signup()
	obj.get_cred()
	status = obj.signup()
	if status == 1:
		print ("Scribble executed successfully!")

def parse_and_execute_login():
	obj = Login()
	obj.get_cred()
	status = obj.login()
	if status == 1:
		print ("Scribble executed successfully!") 

def parse_and_execute_note():
	note_title = None
	keywords = None
	category = None

	parser = optparse.OptionParser()
	parser.add_option('-t', '--title', dest='note_title',
                  help='Enter note title')
	parser.add_option('-k', '--keywords', dest='keywords',
                  help='Enter keywords (separated by comma with no spaces in between')
	parser.add_option('-c', '--category', dest='category',
                  help='Enter category (optional)')

	(options, args) = parser.parse_args()

if len(sys.argv) == 1:
	print ("No action specified. Please specify an action : register, login, note, view, search, delete")
	exit()

action = sys.argv[1]

if action not in ACTIONS:
	print ("Please specify a valid action : register, login, note, view, search, delete")
	exit()

if action == "register":
	parse_and_execute_signup()

if action == "login":
	parse_and_execute_login()

if action == "note":
	parse_and_execute_note()

if action == "view":
	parse_and_execute_view()

if action == "search":
	parse_and_execute_search()

if action == "delete":
	parse_and_execute_delete()
