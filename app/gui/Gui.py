import Tkinter

class Gui:
	def initializeMainWindow(self,w):
		w.title('Knitting pattern uploader')
		w.grid()

		label = Tkinter.Label(w, text=u"Device path (port):")
		label.grid(column=0, row=0, sticky='W')
		
		entryText = Tkinter.StringVar()
		w.deviceEntry = Tkinter.Entry(w, textvariable=entryText)
		w.deviceEntry.grid(column=1,row=0,sticky='EW')
		w.deviceEntry.entryText = entryText
		
#		,text=u"Click me !"
		caption = Tkinter.StringVar()
		self.emuButton = Tkinter.Button(w, textvariable = caption, command = w.emuButtonClicked)
		self.emuButton.caption = caption
		self.emuButton.grid(column=2,row=0)
		self.emuButtonStopped()
		
		label = Tkinter.Label(w, anchor="w",fg="white",bg="blue")
		label.grid(column=0,row=1,columnspan=2,sticky='EW')
		
		w.grid_columnconfigure(0,weight=1)
		w.resizable(True,False)

	def emuButtonStopped(self):
		b = self.emuButton
		b.caption.set(u"Start emulator...")
		
	def emuButtonStarted(self):
		b = self.emuButton
		b.caption.set(u"Stop emulator...")
		
