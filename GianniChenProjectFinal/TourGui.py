'''
Created on May 26, 2016

@author: Gianni
'''

from tkinter import *
from Tour import Tour
from tkinter.messagebox import showinfo
import webbrowser

class TourGui():
    
    def __init__(self):
        'Constructor, also builds the GUI'
        
        # Starts GUI
        root = Tk()
        root.wm_title('Tour')
        
        # Left Frame
        leftFrame = Frame(root)
        
        # Top Frame
        topFrame = Frame(leftFrame, pady = 10, padx = 20)
        orLabel = Label(topFrame, text = 'Origin').pack()
        self.orEntry = Entry(topFrame, width = 28, relief = SUNKEN, borderwidth = 3)
        self.orEntry.pack()
        desLabel = Label(topFrame, text = 'Destination').pack()
        self.desEntry = Entry(topFrame, width = 28, relief = SUNKEN, borderwidth = 3)
        self.desEntry.pack()
        mdLabel = Label(topFrame, text = 'Mode').pack()
        self.mdEntry = Entry(topFrame, width = 28, relief = SUNKEN, borderwidth = 3)
        self.mdEntry.pack()
        
        # Settings Frame
        setLabel = Label(topFrame, text = 'Map Settings', pady = 10).pack()
        settingsFrame = Frame(topFrame, pady = 10)
        
        zmLabel = Label(settingsFrame, text = 'Zoom:').grid(row = 0, column = 0)
        self.zmEntry = Entry(settingsFrame, width = 6, relief = SUNKEN, borderwidth = 3)
        self.zmEntry.grid(row = 0, column = 1)
        self.zmEntry.insert(0, '4')
        zmPlButton = Button(settingsFrame, relief = RAISED, text = '+', width = 2, command = (lambda i = 1: self.zmChange(i))).grid(row = 0, column = 2)
        zmMnButton = Button(settingsFrame, relief = RAISED, text = '-', width = 2, command = (lambda i = -1: self.zmChange(i))).grid(row = 0, column = 3)

        szLabel = Label(settingsFrame, text = 'Size:').grid(row = 1, column = 0)
        self.szEntry = Entry(settingsFrame, width = 6, relief = SUNKEN, borderwidth = 3)
        self.szEntry.grid(row = 1, column = 1)
        self.szEntry.insert(0, '480')
        szPlButton = Button(settingsFrame, relief = RAISED, text = '+', width = 2, command = (lambda i = 40: self.szChange(i))).grid(row = 1, column = 2)
        szMnButton = Button(settingsFrame, relief = RAISED, text = '-', width = 2, command = (lambda i = -40: self.szChange(i))).grid(row = 1, column = 3)

        sclLabel = Label(settingsFrame, text = 'Scale:').grid(row = 2, column = 0)
        self.sclEntry = Entry(settingsFrame, width = 6, relief = SUNKEN, borderwidth = 3)
        self.sclEntry.grid(row = 2, column = 1)
        self.sclEntry.insert(0, '1')
        sclPlButton = Button(settingsFrame, relief = RAISED, text = '1', width = 2, command = (lambda i = 1: self.sclChange(i))).grid(row = 2, column = 2)
        sclMnButton = Button(settingsFrame, relief = RAISED, text = '2', width = 2, command = (lambda i = 2: self.sclChange(i))).grid(row = 2, column = 3)
        settingsFrame.pack(side = BOTTOM)
        
        topFrame.pack()
        
        # Bottom Frame
        botFrame = Frame(leftFrame, pady = 10, padx = 20)
        distLabel = Label(botFrame, text = 'Distance (m)').pack()
        self.distEntry = Entry(botFrame, width = 28, relief = SUNKEN, borderwidth = 3)
        self.distEntry.pack()
        durLabel = Label(botFrame, text = 'Duration (Datetime)').pack()
        self.durEntry = Entry(botFrame, width = 28, relief = SUNKEN, borderwidth = 3)
        self.durEntry.pack()
        buttonFrame = Frame(botFrame, pady = 5)
        distButton = Button(buttonFrame, relief = RAISED, width = 14, text = 'Get Distance', command = self.onClick).pack(side = BOTTOM)
        buttonFrame.pack(side = BOTTOM)
        botFrame.pack()
        leftFrame.pack(side = LEFT)
        
        #Right Frame
        #rightFrame = Frame(root, width = 320, height = 320)
        #self.showUrl = Text(rightFrame)
        #self.showUrl.pack(fill = BOTH)
        #rightFrame.pack(side = RIGHT)
        
        # Main Loop
        root.mainloop()
            
    def onClick(self):
        'Event handler tied to the "Get Distance" button'
        
        # Gets the entry fields
        origin = self.orEntry.get()
        destination = self.desEntry.get()
        mode = self.mdEntry.get()
        #self.showUrl.delete(0.0, END)
        
        # List of allowed modes
        modeList = ['driving', 'biking', 'walking', '']
        
        # An error message pops up if either or both of the entry fields are empty
        if (origin == '' or destination == ''):
            showinfo(title = 'Error: Empty Fields!', message = 'Either or both of the Origin or Destination fields are empty.')
        
        # An error message pops up if the mode is either of the three types or empty
        elif (mode not in modeList):
            showinfo(title = 'Error: Invalid Mode!', message = 'Invalid mode. Valid modes are \'driving\', \'biking\', or \'walking\'.')
        
        # If neither of the errors are encountered, then proceeds to calculated distance
        else:
            
            # Builds an instance of the Tour class and calls its distance method
            aTour = Tour(origin, destination)
            retVal = aTour.distance(mode)
            
            # Separates the distance and the duration
            distance = retVal[0]
            duration = retVal[1]
            
            # Checks if distance is a number, and then inserts its value into distEntry
            if (distance.isdigit()):
                distance = int(distance)
                self.distEntry.delete(0, END)
                self.distEntry.insert(INSERT, '{:,}'.format(distance))
                
                # Inserts the url and automatically opens the map on the web browser
                
                if (self.zmEntry.get().isdigit() and self.szEntry.get().isdigit() and self.sclEntry.get().isdigit()):
                    
                    zmLevel = int(self.zmEntry.get())
                    szLevel = int(self.szEntry.get())
                    sclLevel = int(self.sclEntry.get())
                    
                    if (zmLevel < 1):
                        self.zmEntry.delete(0, END)
                        self.zmEntry.insert(0, '1')
                        zmLevel = 1
                    elif (zmLevel > 20):
                        self.zmEntry.delete(0, END)
                        self.zmEntry.insert(0, '20')
                        zmLevel = 20
                        
                    if (szLevel < 320):
                        self.szEntry.delete(0, END)
                        self.szEntry.insert(0, '320')
                        szLevel = 320
                    elif (szLevel > 640):
                        self.szEntry.delete(0, END)
                        self.szEntry.insert(0, '640')
                        szLevel = 640
                        
                    if (sclLevel < 1):
                        self.sclEntry.delete(0, END)
                        self.sclEntry.insert(0, '1')
                        sclLevel = 1
                    elif (sclLevel > 2):
                        self.sclEntry.delete(0, END)
                        self.sclEntry.insert(0, '2')
                        sclLevel = 2
                        
                    #self.showUrl.insert(0.0, aTour.map(zoom = zmLevel, size = szLevel, scale = sclLevel))
                    webbrowser.open_new(aTour.map(zoom = zmLevel, size = szLevel, scale = sclLevel))
                    
                else:
                    showinfo(title = 'Error: Invalid Settings!', message = 'Please enter valid values in each of the settings.')
                
                # Here it inserts the duration into the durEntry after converting it
                if (duration.isdigit()):
                    duration = int(duration)
                    m, s = divmod(duration, 60)
                    h, m = divmod(m, 60)
                    d, h = divmod(h, 24)
                    duration =  ("%dd %dh %02dm %02ds" % (d, h, m, s))
                else:
                    duration = 0
            
                self.durEntry.delete(0, END)
                self.durEntry.insert(INSERT, duration)
                
            # If the value that is returned is a string, it prints it as an error message instead
            else:
                showinfo(title = 'Error: Distance not found!', message = distance)
                
    def zmChange(self, i):
        if (self.zmEntry.get().isdigit()):
            zmLevel = int(self.zmEntry.get())
            zmLevel += i
            if (zmLevel < 1):
                self.zmEntry.delete(0, END)
                self.zmEntry.insert(0, '1')
            elif (zmLevel > 20):
                self.zmEntry.delete(0, END)
                self.zmEntry.insert(0, '20')
            else:
                self.zmEntry.delete(0, END)
                self.zmEntry.insert(0, zmLevel)
        else:
            showinfo(title = 'Error: Invalid Zoom!', message = 'Please enter a valid integer from 1 to 10 in the zoom setting.')
  
    def szChange(self, i):
        if (self.szEntry.get().isdigit()):
            szLevel = int(self.szEntry.get())
            szLevel += i
            if (szLevel < 320):
                self.szEntry.delete(0, END)
                self.szEntry.insert(0, '320')
            elif (szLevel > 640):
                self.szEntry.delete(0, END)
                self.szEntry.insert(0, '640')
            else:
                self.szEntry.delete(0, END)
                self.szEntry.insert(0, szLevel)
        else:
            showinfo(title = 'Error: Invalid Size!', message = 'Please enter a valid integer from 320 to 640 in the size setting.')
            
    def sclChange(self, i):
        self.sclEntry.delete(0, END)
        self.sclEntry.insert(0, i)