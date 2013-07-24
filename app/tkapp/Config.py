import os

class Config:
	def __init__(self):
		self.imgdir = "img";
		if os.sys.platform == 'win32':
			self.device = "com34"
		else:
			self.device = "/dev/ttyUSB0"