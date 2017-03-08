'''
Created on May 26, 2016

@author: Gianni
'''

from urllib.request import *
import re

class Tour():
    
    def __init__(self, city1, city2):
        'Constructor for the Tour class takes in two cities'
        
        # Places the cities arguments into the class parameters
        self.ct1 = city1
        self.ct2 = city2
        
    def distance(self, mode = 'driving'):
        'Builds the HTML query string and returns the Json string from the Google API. It then looks for and returns the distance value'
        
        # Split cities into lists
        ct1List = re.split(' |, ', self.ct1)
        ct2List = re.split(' |, ', self.ct2)
        
        # Sets up the first part of the HTML query
        queryHTML = 'http://maps.googleapis.com/maps/api/distancematrix/json?origins='
        
        # Loop through origin city
        for i in ct1List:
            queryHTML += i + '+'
            
        # Takes off last '+' and proceeds to set up for destination city
        queryHTML = queryHTML.rstrip('+')
        queryHTML += '&destinations='
        
        # Loop through destination city
        for i in ct2List:
            queryHTML += i + '+'
            
        # Takes off last '+' and proceeds to set up for mode of transportation
        queryHTML = queryHTML.rstrip('+')
        queryHTML += '&mode=' + mode + '&sensor=false'
        
        # Builds a Request object and opens the queryHTML
        user_agent = 'Mozilla/5.0'
        headers = {'User-Agent':user_agent,}
        request = Request(queryHTML,None,headers)
        response = urlopen(request)
        
        # Gets the Json and reads the string
        html = response.read()
        html = html.decode()
        
        # Searches the index where the Json string matches the "value" field
        aDist = re.search('\"value\" : ', html)
        
        # If the Json has a match for the "value" field
        if (aDist):
            
            # Searches the index for the rest of the Json string for the first newline char
            bDist = re.search('\n',(html[aDist.end():]))
            
            # The distance is the value that is sandwiched between the two indexes found above
            valDist = (html[aDist.end():(aDist.end() + bDist.end() - 1)])
            
            # Searches for the next "value" field starting from the 'aDist' index, so that it skips the distance value
            aDur = re.search('\"value\" : ', html[aDist.end():])
            
            # If the duration is found, it will search the index for the next newline char and will also get its value into valDur
            if (aDur):
                bDur = re.search('\n',(html[(aDist.end() + aDur.end()):]))
                valDur = (html[(aDist.end() + aDur.end()):(aDist.end() + aDur.end() + bDur.end() - 1)])
                
            # In case the duration is not found, it just returns 0
            else:
                valDur = 0
                
            return (valDist, valDur)
        
        # If the Json does not have a match for the "value" field returns an error message string
        else:
            retval = 'Distance between '
            for i in ct1List:
                retval += i + ' '
            retval += 'and '
            for i in ct2List:
                retval += i + ' '
            retval += 'was not found.'
            
            return (retval, 0)
        
    def latlng(self, List):
        
        qrList = re.split(' |, ', List)
        queryHTML = 'https://maps.googleapis.com/maps/api/geocode/json?address='
        for i in qrList:
            queryHTML += i + '+'
        queryHTML = queryHTML.rstrip('+')
        queryHTML += '&key=AIzaSyB8bzshI-dm0je_2GQDbO5G_w1WuFqrZ7c'
        user_agent = 'Mozilla/5.0'
        headers = {'User-Agent':user_agent,}
        request = Request(queryHTML,None,headers)
        response = urlopen(request)
        html = response.read()
        html = html.decode()
        aLoc = re.search('\"location\" : ', html)
        if(aLoc):
            aLat = re.search('\"lat\" : ', html[aLoc.end():])
            bLat = re.search(',', html[(aLoc.end() + aLat.end()):])
            lat = html[(aLoc.end() + aLat.end()):(aLoc.end() + aLat.end() + bLat.end() - 1)]
            aLng = re.search('\"lng\" : ', html[aLoc.end():])
            bLng = re.search('\n', html[(aLoc.end() + aLng.end()):])
            lng = html[(aLoc.end() + aLng.end()):(aLoc.end() + aLng.end() + bLng.end() - 1)]
            return (lat, lng)
    
    def map(self, zoom = 4, size = 480, scale = 1):
        
        latlng1 = self.latlng(self.ct1)
        latlng2 = self.latlng(self.ct2)
        avglat = (float(latlng1[0]) + float(latlng2[0]))/2
        avglng = (float(latlng1[1]) + float(latlng2[1]))/2
        
        queryHTML = 'https://maps.googleapis.com/maps/api/staticmap?'
        queryHTML += 'center=' + str(avglat) + ',' + str(avglng) 
        queryHTML += '&zoom=' + str(zoom)
        queryHTML += '&size=' + str(size) + 'x' + str(size)
        queryHTML += '&scale=' + str(scale)
        queryHTML += '&markers=color:red%7Clabel:O%7C' + latlng1[0] + ',' + latlng1[1]
        queryHTML += '&markers=color:red%7Clabel:D%7C' + latlng2[0] + ',' + latlng2[1] 
        queryHTML += '&key=AIzaSyB8bzshI-dm0je_2GQDbO5G_w1WuFqrZ7c'
        
        return (queryHTML)