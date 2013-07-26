import Tkinter

class Gui:
    def initializeMainWindow(self,w):
        self.initMainWindow(w)

        self._maxColumns = 1000
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
        self.mainWindow.geometry("800x400")
        self.mainWindow.grid()
        self.mainWindow.grid_columnconfigure(1,weight=1)
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
        self.emuButton.grid(column=2,row=self._row)
        self.setEmuButtonStopped()
        
    def createDatFileWidgets(self):
        label = Tkinter.Label(self.mainWindow, text=u"Dat file:")
        label.grid(column=0, row=self._row, sticky='W')
        
        entryText = Tkinter.StringVar()
        self.mainWindow.datFileEntry = Tkinter.Entry(self.mainWindow, textvariable=entryText)
        self.mainWindow.datFileEntry.grid(column=1,row=self._row,sticky='EW')
        self.mainWindow.datFileEntry.entryText = entryText

        self.reloadDatFileButton = Tkinter.Button(self.mainWindow, text=u"Reload file", command = self.mainWindow.reloadDatFileButtonClicked)
        self.reloadDatFileButton.grid(column=2,row=self._row,sticky='EW')
        
    def createInfoMessagesLabel(self):
        labelText = Tkinter.StringVar()
        label = Tkinter.Label(self.mainWindow, anchor="w",fg="white",bg="blue",textvariable=labelText)
        label.grid(column=0,row=self._row,columnspan=self._maxColumns,sticky='EW')
        label.caption = labelText
        self.mainWindow.infoLabel = label
        
    def createPatternsPanel(self):
        patternFrame = Tkinter.Frame(self.mainWindow)
        patternFrame.grid(column=0, row=self._row, columnspan = self._maxColumns,sticky='EW')
        patternFrame.grid_columnconfigure(0,weight=1)
        patternFrame.grid_columnconfigure(1,weight=1)
        
        listvar = Tkinter.StringVar()
        lb = Tkinter.Listbox(patternFrame, listvariable=listvar, exportselection=0, width=50)
        lb.items = ListboxVar(lb, listvar)
        lb.grid(column=0, row=0, sticky='EW')
        lb.bind('<<ListboxSelect>>', self.mainWindow.patternSelected)
        self.mainWindow.patternListBox = lb;
        
        pc = ExtendedCanvas(patternFrame, bg='white')
        pc.grid(column=1, row=0, sticky='EW')
        self.mainWindow.patternCanvas = pc
    
    def setEmuButtonStopped(self):
        b = self.emuButton
        b.caption.set(u"Start emulator...")
        
    def setEmuButtonStarted(self):
        b = self.emuButton
        b.caption.set(u"Stop emulator...")
        
class ExtendedCanvas(Tkinter.Canvas):
    def getWidth(self):
        return int(self.cget('width'))
        
    def getHeight(self):
        return int(self.cget('height'))
        
    def clear(self):
        self.create_rectangle(0,0,self.getWidth(),self.getHeight(), width=0, fill=self.cget('bg'))
        
class ListboxVar:
    def __init__(self, listbox, stringvar):
        self._stringvar = stringvar
        self._listbox = listbox
        
    def set(self, list):
        self._listbox.delete(0, Tkinter.END)
        for item in list:
            self._listbox.insert(Tkinter.END, item)
