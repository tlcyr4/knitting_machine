import tkMessageBox as mb
import sys

class Messages:
    def __init__(self, knittinApp):
        self.app = knittinApp
        self.displayMessages = True
        
    def showError(self, msg):
        if self.displayMessages:
            self.clear()
            sys.stderr.write('Error: ' + str(msg) + '\n')
            mb.showerror('Error:', str(msg))
        
    def showInfo(self, msg):
        if self.displayMessages:
            self.clear()
            print msg
            self.app.infoLabel.caption.set('Info: ' + str(msg))
        
    def clear(self):
        if self.displayMessages:
            self.app.infoLabel.caption.set('')
        