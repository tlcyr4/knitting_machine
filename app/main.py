#!/usr/bin/python
# -*- coding: UTF-8 -*-

import Tkinter
from pdd import PDDemulate as pdd
import config
import serial

c = config.Config()

class KnittingApp(Tkinter.Tk):

	def __init__(self,parent):
		Tkinter.Tk.__init__(self,parent)
		self.parent = parent
		self.initialize()
		self.runEmulator()

	def initialize(self):
		self.grid()
		
		self.entry = Tkinter.Entry(self)
		self.entry.grid(column=0,row=0,sticky='EW')
		
		button = Tkinter.Button(self,text=u"Click me !")
		button.grid(column=1,row=0)
		
		label = Tkinter.Label(self, anchor="w",fg="white",bg="blue")
		label.grid(column=0,row=1,columnspan=2,sticky='EW')
		
		self.grid_columnconfigure(0,weight=1)
		self.resizable(True,False)
		
	def runEmulator(self):
		print 'Preparing emulator. . . Please Wait'
		try:
			self.emu = pdd.PDDemulator(c.imgdir)
			
			self.emu.open(cport=c.device)
			print 'PDDemulate Version 1.1 Ready!'
			self.after(5, self.runEmulator)
		except Exception, e:
			print "Exception:", e
			self.quitApplication()
		
	def emulatorLoop(self):
		emu.handleRequests()
		
	def quitApplication(self):
		if self.emu is not None:
			self.emu.close()
		self.after_idle(self.quit)


if __name__ == "__main__":
	app = KnittingApp(None)
	app.title('Knitting pattern uploader')
	app.mainloop()