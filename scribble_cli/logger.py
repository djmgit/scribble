
class Logger:

	def __init__(self):

		self.colors = {
			"HEADER" = "\033[95m"
    		"OKBLUE" = "\033[94m"
    		"OKGREEN" = "\033[92m"
    		"WARNING" = "\033[93m"
    		"FAIL" = "\033[91m"
    		"ENDC" = "\033[0m"
    		"BOLD" = "\033[1m"
    		"UNDERLINE" = "\033[4m"
		}

	def success(self, message):
		print ("{} {} {}").format(self.colors["OKGREEN"], message, self.colors["ENDC"])

	def fail(self, message):
		print ("{} {} {}").format(self.colors["FAIL"], message, self.colors["ENDC"])

	def warning(self, message):
		print ("{} {} {}").format(self.colors["WARNING"], message, self.colors["ENDC"])

	def header(self, message):
		print ("{} {} {}").format(self.colors["HEADER"], message, self.colors["ENDC"])

	def info(self, message):
		print ("{} {} {}").format(self.colors["OKBLUE"], message, self.colors["ENDC"])
