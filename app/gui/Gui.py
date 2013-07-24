import Tkinter

class Gui:
	def initializeMainWindow(self,w):
		w.title('Knitting pattern uploader')
		w.grid()

		row = 0
		
		label = Tkinter.Label(w, text=u"Device path (port):")
		label.grid(column=0, row=row, sticky='W')
		
		entryText = Tkinter.StringVar()
		w.deviceEntry = Tkinter.Entry(w, textvariable=entryText)
		w.deviceEntry.grid(column=1,row=row,sticky='EW')
		w.deviceEntry.entryText = entryText
		
#		,text=u"Click me !"
		caption = Tkinter.StringVar()
		self.emuButton = Tkinter.Button(w, textvariable = caption, command = w.emuButtonClicked)
		self.emuButton.caption = caption
		self.emuButton.grid(column=2,row=row)
		self.emuButtonStopped()

		row = 1
		
		label = Tkinter.Label(w, text=u"Dat file:")
		label.grid(column=0, row=row, sticky='W')
		
		entryText = Tkinter.StringVar()
		w.datFileEntry = Tkinter.Entry(w, textvariable=entryText)
		w.datFileEntry.grid(column=1,row=row,sticky='EW',columnspan=2)
		w.datFileEntry.entryText = entryText
		
		row = 2
		
		labelText = Tkinter.StringVar()
		label = Tkinter.Label(w, anchor="w",fg="white",bg="blue",textvariable=labelText)
		label.grid(column=0,row=row,columnspan=3,sticky='EW')
		label.caption = labelText
		w.infoLabel = label
		
		w.grid_columnconfigure(0,weight=1)
		w.resizable(True,False)

	def emuButtonStopped(self):
		b = self.emuButton
		b.caption.set(u"Start emulator...")
		
	def emuButtonStarted(self):
		b = self.emuButton
		b.caption.set(u"Stop emulator...")
		
