# Electroknit

Please see the Changelog file for the latest changes


## Quick Start


Install python dependencies with pip and execute script guimain.py to start the
graphical application.  If you do not have pip, follow install instructions at
http://www.pip-installer.org/

```
pip install -r requirements.txt
python guimain.py
```

##Introduction

The Brother knitting machines can save data to an external floppy disk drive, which connects to the machine using a serial cable.

These external floppy drives are difficult to find and expensive, and the physical format of the floppy disks is different than 3.25" PC drives.

The program PDDemulate acts like a floppy drive, and runs on linux machines, allowing you to save and restore data from the knitting machine.

Most of the formatting of the saved data files has been figured out, and the tools used to do that are also in this repository.

There is also an example of how to generate a text banner in a .png image file, 
which may be useful to some.

This application can start floppy disk emulator and provides means to download/upload patterns and modify them.
It is based on existing python scripts, which were slightly modified for better user experience in graphical application.

These files are related to the Brother KH-930E knitting machine, and other similar models.

The emulator script was named PDDemulate-1.0.py, and the instructions in a lot of forums for using it have that name.
The script has been renamed, and is now simply PDDemulate.py.

----

The files in the top directory are the ones used for the knitting project that Becky Stern and Limor Fried did:

http://makezine.com/craft/hack_your_knitting_machine/
https://web.archive.org/web/20101111163531/http://blog.craftzine.com/archive/2010/11/hack_your_knitting_machine.html

##Subdirectories

* **docs**:
Documentation for the project, including the data file format information and scans of old manuals which are hard to find.

* **experimental**:
  Some never-tested code to talk to a Tandy PDD-1 or Brother disk drive.

* **file-analysis**:
  Various scripts used to reverse-engineer the brother data format, as well as some spreadsheets used.
  These may or may nor work, but may be useful for some.

* **test-data**:
  A saved set of data from the PDDemulator, with dicumentation abotu what's saved in each memory location.
  A good way to play with the file analysis tools, and may give some insight into the reverse engineering
  process.

* **textconversion:**
  The beginnings of work to convert text to a knittable banner.

--------------------------

The work that Steve Conklin did was based on earlier work by John R. Hogerhuis.

This extended by Becky and Limor and others, including Travis Goodspeed:

http://travisgoodspeed.blogspot.com/2010/12/hacking-knitting-machines-keypad.html
