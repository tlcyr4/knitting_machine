#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Config import Config
from Messages import Messages
from gui.Gui import Gui
from pdd.PDDemulate import PDDemulator
import Tkinter

class KnittingApp(Tkinter.Tk):

	def __init__(self,parent=None):
		Tkinter.Tk.__init__(self,parent)
		self.parent = parent
		self.initialize()
		#self.startEmulator()
		
	def initialize(self):
		self.msg = Messages()
		self._cfg = None
		self.gui = Gui()
		self.gui.initializeMainWindow(self)
		self.deviceEntry.entryText.set(self.getConfig().device)
		self.initEmulator()
		
	def initEmulator(self):
		self.emu = PDDemulator(self.getConfig().imgdir)
		self.setEmulatorStarted(False)
		
	def emuButtonClicked(self):
		self.getConfig().device = self.deviceEntry.entryText.get()
		if self.emu.started:
			self.stopEmulator()
		else:
			self.startEmulator()
		
	def startEmulator(self):
		print 'Preparing emulator. . . Please Wait'
		try:
			self.emu.open(cport=self.getConfig().device)
			print 'PDDemulate Version 1.1 Ready!'
			self.setEmulatorStarted(True)
			self.after(5, self.emulatorLoop)
		except Exception, e:
			print "Exception:", e
			
			self.setEmulatorStarted(False)
		
	def emulatorLoop(self):
		self.emu.handleRequest()
		
	def stopEmulator(self):
		if self.emu is not None:
			self.emu.close()
			print 'PDDemulate stopped.'
			self.setEmulatorStarted(False)
		self.initEmulator()
		
	def quitApplication(self):
		self.stopEmulator()
		self.after_idle(self.quit)
		
	def setEmulatorStarted(self, started):
		self.emu.started = started
		if started:
			self.gui.emuButtonStarted()
		else:
			self.gui.emuButtonStopped()
	
	def getConfig(self):
		if self._cfg is None:
			self._cfg = Config()
			if not hasattr(self._cfg, "device"):
				self._cfg.device = u""
		return self._cfg
		

	
if __name__ == "__main__":
	app = KnittingApp(None)
	app.mainloop()