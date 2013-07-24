import tkMessageBox as mb
import sys

class Messages:
	def __init__(self, knittinApp):
		self.app = knittinApp
		
	def showError(self, msg):
		self.clear()
		sys.stderr.write('Error: ' + str(msg) + '\n')
		mb.showerror('Error:', str(msg))
		
	def showInfo(self, msg):
		self.clear()
		print msg
		self.app.infoLabel.caption.set('Info: ' + str(msg))
		
	def clear(self):
		self.app.infoLabel.caption.set('')
		