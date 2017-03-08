'''
Created on May 16, 2016

@author: Gianni
'''

from urllib.request import *
from html.parser import HTMLParser
import re
from tkinter import *

class MyHTMLParser(HTMLParser):
    
    global queryResults
    
    def handle_starttag(self, tag, attrs):
        'Looks through the html item and finds href tags. It then prints out the stripped links'
        
        if (tag == 'a'):
            for attr in attrs:
                if (attr[0] == 'href'):
                    
                    # Here it tries to search and match the Google results links, where they begin at 'a' and end at 'b'
                    a = re.match('/url\?q=https?://', attr[1])
                    b = re.search('&sa', attr[1])
                    
                    # Only the ones matching the pattern found in 'a' will return a result
                    if (a):
                        
                        # These statements below ignore any links that start with webcache since these are just repeats of the link directly above
                        c = re.match('webcache', attr[1][a.end():b.start()])
                        if (not c):
                            queryResults.insert(INSERT, (attr[1][a.end():b.start()]))
                            queryResults.insert(INSERT, '\n')

def buildHTTP(inputList):
    'Reads a list of keywords and returns a google search query in html'

    # Initializes starting query html address
    queryHTML = 'http://www.google.com/search?q='
    
    # Loops through the list of keywords and appends them into the html address string
    for words in inputList:
        queryHTML += words + '+'
        
    # Strips the last '+' sign
    queryHTML = queryHTML.rstrip('+')
    
    return queryHTML

def googlSearch():
    'Main Searching Method'
    
    global queryEntry
    global queryResults
    
    queryResults.delete('1.0', END)

    if (queryEntry.get() != ''):

        # Prompts user for keyword inputs, breaks them into a list and builds the html string
        inputString = queryEntry.get()
        aList = inputString.split()
        url = buildHTTP(aList)
        
        # Builds a Request object and opens the url
        user_agent = 'Mozilla/5.0'
        headers = {'User-Agent':user_agent,}
        request = Request(url,None,headers)
        response = urlopen(request)
        
        # Prints the list of keywords
        keywordString = 'Google has returned the following links for the keywords \''
        for words in aList:
            keywordString += words + ' '
        
        keywordString = keywordString.rstrip(' ')
        keywordString += '\':\n'
            
        queryResults.insert(INSERT, keywordString)
        queryResults.insert(INSERT, '\n')
        
        # Reads and decodes the response; it then runs it through the HTMLParser class in order to print the links
        html = response.read()
        html = html.decode()
        linkparser = MyHTMLParser()
        linkparser.feed(html)
    
def googlClear():
    'Clears the queryResults textbox'
    
    global queryResults
    
    queryResults.delete('1.0', END)
    
# Start of main loop

# Constructor to instantiate a master
root = Tk()
root.wm_title('Google in Python')
root.configure(background = 'white')
    
# Creates a Frame and adds to the top of root
topFrame = Frame(root)
topFrame.configure(background = 'white')
topFrame.pack(side = TOP)

# Google logo label
logoImage = PhotoImage(file = 'Google_Logo.gif')
logoLabel = Label(topFrame, image = logoImage)
logoLabel.configure(background = 'white')
logoLabel.pack(side = TOP)

# Contains the queryEntry and the buttonFrame frames
programFrame = Frame(topFrame)
programFrame.configure(background = 'white')
programFrame.pack(side = BOTTOM)

# Entry Frame
queryEntry = Entry(programFrame, width = 70, relief = SUNKEN, borderwidth = 3)
queryEntry.pack(side = TOP)
queryEntry.insert(INSERT, '')

# Buttons Frame
buttonFrame = Frame(programFrame)
buttonFrame.configure(background = 'white')
buttonFrame.pack(side = BOTTOM)

# Creates a Frame and adds to the bottom of root
botFrame = Frame(root)
botFrame.pack(side = TOP)

# Query results Frame
queryResults = Text(botFrame, width = 100)
queryResults.pack()
queryResults.insert(INSERT, '')
    
# Creates Buttons
search = Button(buttonFrame,
                relief = RAISED,
                padx = 10,
                pady = 5,
                width = 14,
                text = 'Search',
                command = googlSearch).pack(side = LEFT)
                    
lucky = Button(buttonFrame,
                relief = RAISED,
                padx = 10,
                pady = 5,
                width = 14,
                text = 'Clear',
                command = googlClear).pack(side = RIGHT)
    
root.mainloop()
