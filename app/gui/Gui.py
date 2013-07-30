import Tkinter

class Gui:
    def initializeMainWindow(self,w):
        self.initMainWindow(w)

        self._maxColumns = 1000
        self._maxRows = 1000
        self._row = 0
        self.createDeviceWidgets()
        self.createEmulatorButton()

        self._row += 1
        self.createDatFileWidgets()
        
        self._row += 1
        self.createPatternsPanel()

        self._row += 1
        self.createInfoMessagesLabel()

    def initMainWindow(self, mainWindow):
        self.mainWindow = mainWindow
        self.mainWindow.title('Knitting pattern uploader')
        self.mainWindow.geometry("600x400")
        self.mainWindow.grid()
        self.mainWindow.grid_columnconfigure(1,weight=10)
        self.mainWindow.grid_columnconfigure(2,weight=1)
        self.mainWindow.resizable(True,True)
        
    def createDeviceWidgets(self):
        label = Tkinter.Label(self.mainWindow, text=u"Device path (port):")
        label.grid(column=0, row=self._row, sticky='W')
        
        entryText = Tkinter.StringVar()
        self.mainWindow.deviceEntry = Tkinter.Entry(self.mainWindow, textvariable=entryText)
        self.mainWindow.deviceEntry.grid(column=1,row=self._row,sticky='EW')
        self.mainWindow.deviceEntry.entryText = entryText
        
    def createEmulatorButton(self):
        caption = Tkinter.StringVar()
        self.emuButton = Tkinter.Button(self.mainWindow, textvariable = caption, command = self.mainWindow.emuButtonClicked)
        self.emuButton.caption = caption
        self.emuButton.grid(column=2,row=self._row, columnspan=2, sticky='EW')
        self.setEmuButtonStopped()
        
        but = Tkinter.Button(self.mainWindow, text = u'Help...', command = self.mainWindow.helpButtonClicked)
        but.grid(column=4,row=self._row, sticky='E')
        
    def createDatFileWidgets(self):
        label = Tkinter.Label(self.mainWindow, text=u"Dat file:")
        label.grid(column=0, row=self._row, sticky='W')
        
        entryText = Tkinter.StringVar()
        self.mainWindow.datFileEntry = Tkinter.Entry(self.mainWindow, textvariable=entryText)
        self.mainWindow.datFileEntry.grid(column=1,row=self._row,sticky='EW')
        self.mainWindow.datFileEntry.entryText = entryText

        self.chooseDatFileButton = Tkinter.Button(self.mainWindow, text=u"...", command = self.mainWindow.chooseDatFileButtonClicked)
        self.chooseDatFileButton.grid(column=2,row=self._row,sticky='W')

        self.reloadDatFileButton = Tkinter.Button(self.mainWindow, text=u"Reload file", command = self.mainWindow.reloadDatFileButtonClicked)
        self.reloadDatFileButton.grid(column=3,row=self._row,sticky='EW')
        
    def createInfoMessagesLabel(self):
        labelText = Tkinter.StringVar()
        label = Tkinter.Label(self.mainWindow, anchor="w",fg="white",bg="blue",textvariable=labelText)
        label.grid(column=0,row=self._row,columnspan=self._maxColumns,sticky='EW')
        label.caption = labelText
        self.mainWindow.infoLabel = label
        
    def createPatternsPanel(self):
        patternFrame = Tkinter.Frame(self.mainWindow)
        patternFrame.grid(column=0, row=self._row, columnspan = self._maxColumns,sticky='EWNS')
        self.mainWindow.grid_rowconfigure(self._row,weight=1)
        patternFrame.grid_columnconfigure(0,weight=1)
        patternFrame.grid_columnconfigure(1,weight=1)
        patternFrame.grid_rowconfigure(1,weight=1)
        
        listboxFrame = Tkinter.Frame(patternFrame)
        listboxFrame.grid(column=0, row=0, sticky='EWNS', rowspan=self._maxRows)
        scrollbar = Tkinter.Scrollbar(listboxFrame, orient=Tkinter.VERTICAL)
        listvar = Tkinter.StringVar()
        lb = Tkinter.Listbox(listboxFrame, listvariable=listvar, exportselection=0, width=50, yscrollcommand=scrollbar.set)
        scrollbar.config(command=lb.yview)
        lb.items = ListboxVar(lb, listvar)
        scrollbar.pack(side=Tkinter.RIGHT, fill=Tkinter.Y)
        lb.pack(side=Tkinter.LEFT, fill=Tkinter.BOTH, expand=1)
        self.mainWindow.patternListBox = lb;

        textvar = Tkinter.StringVar()
        label = Tkinter.Label(patternFrame, anchor="w", textvariable = textvar)
        label.grid(column=1, row=0, sticky='EW')
        label.caption = textvar
        self.mainWindow.patternTitle = label
        
        self.insertBitmapButton = Tkinter.Button(patternFrame, text=u"Insert bitmap...", command = self.mainWindow.insertBitmapButtonClicked)
        self.insertBitmapButton.grid(column=2,row=0,sticky='EW')

        pc = ExtendedCanvas(patternFrame, bg='white')
        pc.grid(column=1, row=1, sticky='EWNS', columnspan=2)
        self.mainWindow.patternCanvas = pc
        
    def setEmuButtonStopped(self):
        b = self.emuButton
        b.caption.set(u"Start emulator...")
        
    def setEmuButtonStarted(self):
        b = self.emuButton
        b.caption.set(u"...stop emulator")
        
class ExtendedCanvas(Tkinter.Canvas):

    def getWidth(self):
        w = self.winfo_width()
        return w
        
    def getHeight(self):
        h = self.winfo_height()
        return h
        
    def clear(self):
        maxsize = 10000
        self.create_rectangle(0,0,maxsize, maxsize, width=0, fill=self.cget('bg'))
        
class ListboxVar:
    def __init__(self, listbox, stringvar):
        self._stringvar = stringvar
        self._listbox = listbox
        
    def set(self, list):
        self._listbox.delete(0, Tkinter.END)
        for item in list:
            self._listbox.insert(Tkinter.END, item)
