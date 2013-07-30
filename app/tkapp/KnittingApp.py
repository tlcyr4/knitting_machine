#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Config import Config
from Messages import Messages
from app.gui.Gui import Gui
from PDDemulate import PDDemulator
from PDDemulate import PDDEmulatorListener
from dumppattern import PatternDumper
from insertpattern import PatternInserter
import Tkinter
import tkFileDialog

class KnittingApp(Tkinter.Tk):

    def __init__(self,parent=None):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()
        #self.startEmulator()
        
    def initialize(self):
        self.msg = Messages(self)
        self.patterns = []
        self.pattern = None
        self._cfg = None
        self.currentDatFile = None
        self.initializeUtilities()
        self.gui = Gui()
        self.gui.initializeMainWindow(self)
        self.updatePatternCanvasLastSize()
        self.patternListBox.bind('<<ListboxSelect>>', self.patternSelected)
        self.after_idle(self.canvasConfigured)
        self.deviceEntry.entryText.set(self.getConfig().device)
        self.datFileEntry.entryText.set(self.getConfig().datFile)
        self.initEmulator()
        self.after_idle(self.reloadPatternFile)
        
    def initializeUtilities(self):
        self.patternDumper = PatternDumper()
        self.patternDumper.printInfoCallback = self.msg.showInfo
        self.patternInserter = PatternInserter()
        self.patternInserter.printInfoCallback = self.msg.showInfo
        self.patternInserter.printErrorCallback = self.msg.showError
        
    def initEmulator(self):
        self.emu = PDDemulator(self.getConfig().imgdir)
        self.emu.listeners.append(PDDListener(self))
        self.setEmulatorStarted(False)
    
    def emuButtonClicked(self):
        self.getConfig().device = self.deviceEntry.entryText.get()
        if self.emu.started:
            self.stopEmulator()
        else:
            self.startEmulator()
        
    def startEmulator(self):
        self.msg.showInfo('Preparing emulator. . . Please Wait')

        if self.getConfig().simulateEmulator:
            self.msg.showInfo('Simulating emulator, emulator is not started...')
            self.setEmulatorStarted(True)
        else:
            try:
                port = self.getConfig().device
                self.emu.open(cport=port)
                self.msg.showInfo('PDDemulate Version 1.1 Ready!')
                self.setEmulatorStarted(True)
                self.after_idle(self.emulatorLoop)
            except Exception, e:
                self.msg.showError('Ensure that TFDI cable is connected to port ' + port + '\n\nError: ' + str(e))
                self.setEmulatorStarted(False)
        
    def emulatorLoop(self):
        if self.emu.started:
            self.emu.handleRequest()
            self.after_idle(self.emulatorLoop)
        
    def stopEmulator(self):
        if self.emu is not None:
            self.emu.close()
            self.msg.showInfo('PDDemulate stopped.')
            self.setEmulatorStarted(False)
        self.initEmulator()
        
    def quitApplication(self):
        self.stopEmulator()
        self.after_idle(self.quit)
        
    def setEmulatorStarted(self, started):
        self.emu.started = started
        if started:
            self.gui.setEmuButtonStarted()
        else:
            self.gui.setEmuButtonStopped()
    
    def getConfig(self):
        cfg = self._cfg
        if cfg is None:
            self._cfg = cfg = Config()
            if not hasattr(cfg, "device"):
                cfg.device = u""
            if not hasattr(cfg, "datFile"):
                cfg.datFile = u""
            if not hasattr(cfg, "simulateEmulator"):
                cfg.simulateEmulator = False
        return cfg
        
    def reloadPatternFile(self, pathToFile = None):
        if not pathToFile:
            pathToFile = self.datFileEntry.entryText.get()
        else:
            self.datFileEntry.entryText.set(pathToFile)

        if not pathToFile:
            return
        self.currentDatFile = pathToFile
        try:
            result = self.patternDumper.dumppattern([pathToFile])
            self.patterns = result.patterns
            listBoxModel = []
            for p in self.patterns:
                listBoxModel.append(self.getPatternTitle(p))
            self.patternListBox.items.set(listBoxModel)
            if (len(listBoxModel) > 0):
                selected_index = 0
                self.patternListBox.selection_set(selected_index)
                self.displayPattern(self.patterns[selected_index])
            else:
                self.displayPattern(None)
        except IOError as e:
            self.msg.showError('Could not open pattern file %s' % pathToFile + '\n' + str(e))
        
    def helpButtonClicked(self):
        helpMsg = '''Commands to execute on Knitting machine:

552: Download patterns from machine to computer
551: Upload patterns from computer to machine
'''
        self.msg.showMoreInfo(helpMsg)

    def reloadDatFileButtonClicked(self):
        self.reloadPatternFile()

    def chooseDatFileButtonClicked(self):
        filePath = tkFileDialog.askopenfilename(filetypes=[('DAT file', '*.dat')], initialfile=self.datFileEntry.entryText.get(),
            title='Choose dat file with patterns...')
        if len(filePath) > 0:
            self.msg.showInfo('Opened dat file ' + filePath)
            self.reloadPatternFile(filePath)
        
    def patternSelected(self, evt):
        w = evt.widget
        sel = w.curselection()
        if len(sel) > 0:
            index = int(sel[0])
            pattern = self.patterns[index]
        else:
            pattern = None
        self.displayPattern(pattern)
        
    def displayPattern(self, pattern=None):
        if not pattern:
            pattern = self.pattern
        self.patternCanvas.clear()
        self.patternTitle.caption.set(self.getPatternTitle(pattern))
        if pattern:
            result = self.patternDumper.dumppattern([self.currentDatFile, str(pattern['number'])])
            self.printPatternOnCanvas(result.pattern)
        self.pattern = pattern
        
    def getPatternTitle(self, pattern):
        p = pattern
        if p:
            return 'Pattern no: ' + str(p['number']) + " (rows x stitches: " + str(p["rows"]) + " x " + str(p["stitches"]) + ")" 
        else:
            return 'No pattern'
    
    def printPatternOnCanvas(self, pattern):
        patternWidth = len(pattern)
        patternHeight = len(pattern[0])
        bitWidth = self.patternCanvas.getWidth() / patternWidth;
        bitHeight = self.patternCanvas.getHeight() / patternHeight;
        self.patternCanvas.clear()
        for row in range(len(pattern)):
            for stitch in range(len(pattern[row])):
                if(pattern[row][stitch]) == 0:
                    self.patternCanvas.create_rectangle(stitch * bitWidth,row * bitHeight,(stitch+1) * bitWidth,(row+1) * bitHeight, width=0, fill='black')
                    
    def updatePatternCanvasLastSize(self):
        self.patternCanvas.lastWidth = self.patternCanvas.getWidth()
        self.patternCanvas.lastHeight = self.patternCanvas.getHeight()
                    
    def canvasConfigured(self):
        if self.patternCanvas.lastWidth != self.patternCanvas.getWidth() or self.patternCanvas.lastHeight != self.patternCanvas.getHeight():
            self.msg.displayMessages = False
            self.updatePatternCanvasLastSize()
            self.displayPattern()
            self.msg.displayMessages = True
        self.after(100, self.canvasConfigured)
    
    def insertBitmapButtonClicked(self):
        sel = self.patternListBox.curselection()
        if len(sel) == 0:
            self.msg.showError('Target pattern for insertion must be selected!')
            return
        index = int(sel[0])
        pattern = self.patterns[index]
        filePath = tkFileDialog.askopenfilename(filetypes=[('2-color Bitmap', '*.bmp')],
            title='Choose bitmap file to insert...')
        if len(filePath) > 0:
            self.insertBitmap(filePath, pattern["number"])
            
    def insertBitmap(self, bitmapFile, patternNumber):
        self.msg.showInfo('Inserting dat file %s to pattern number %d' % (bitmapFile, patternNumber))
        oldBrotherFile = self.currentDatFile
        self.patternInserter.insertPattern(oldBrotherFile, patternNumber, bitmapFile, 'myfile.dat')

class PDDListener(PDDEmulatorListener):

    def __init__(self, app):
        self.app = app

    def dataReceived(self, fullFilePath):
        self.reloadPatternFile(fullFilePath)
    
    
if __name__ == "__main__":
    app = KnittingApp()
    app.mainloop()