'''
Created on May 16, 2016

@author: Gianni
'''

from urllib.request import *
from html.parser import HTMLParser
import re

class MyHTMLParser(HTMLParser):
    
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
                            print (attr[1][a.end():b.start()])
                        
def promptUser():
    'Prompts the user for the words to search on Google'
    
    # Loops for inputs unless there are no errors
    while True:
            try:
                inputString = input('Please input the keywords separated by an empty space: \n')
            except OSError:
                print('You encountered an error, please try again.\n')
                continue
            else:
                break
    return inputString

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
    
def main():
    
    print ('Welcome to Google!')
    
    # Prompts user for keyword inputs, breaks them into a list and builds the html string
    inputString = promptUser()
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
        
    print (keywordString)
    
    # Reads and decodes the response; it then runs it through the HTMLParser class in order to print the links
    html = response.read()
    html = html.decode()
    linkparser = MyHTMLParser()
    linkparser.feed(html)
    
    command = input('\nPress any key to exit the application\n')
    
# Main Part of the program   
main()
