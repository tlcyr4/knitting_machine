import os

class Config:
    def __init__(self):
        self.imgdir = "img";
        if os.sys.platform == 'win32':
            self.device = "com34"
            self.datFile = 'c:\\Documents and Settings\\ondro\\VirtualBox shared folder\\knitting\\app\\img\\file-01.dat'
            self.simulateEmulator = True
        else:
            self.device = "/dev/ttyUSB0"