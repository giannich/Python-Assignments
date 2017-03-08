'''
Created on Apr 23, 2016

@author: Gianni
'''

import re

def getInputDescriptor(validation):
    'Prompts user for file name and returns file'
    
    #If validation is true, then prompts the user for filename, otherwise automatically loads the ref file
    if validation:
        while True:
            try:
                inputFileName = input('Please input the name of the sample file: \n')
                inFile = open(inputFileName, 'r')
            except OSError:
                print('You entered an invalid name. Please try again.')
                continue
            else:
                break
            
        return inFile
    
    else:
        inFile = open('ref.txt', 'r')
        return inFile

def readFrequency(fileObject):
    'Reads the file and stores each word in a dictionary with frequency'
    
    fileLineList = []
    sentencesList = []
    wordList = []
    returnDict = {}
    
    #Inputs lines into a list of lines
    fileLineList = fileObject.readlines()
    
    #Strips punctuation from each of the lines in the list
    sentencesList = [re.sub('([,.!?:]){1,}', '', sentence).strip() for sentence in fileLineList]
    
    #Separates the list of sentences into a list of their respective lowercase words
    for sentences in sentencesList:
        for words in sentences.split():
            wordList.append(words.lower())
    
    #Loops through the list of words and updates the frequency dict
    for word in wordList:
        if word in returnDict:
            returnDict[word] += 1
        else:
            returnDict[word] = 1
    
    return returnDict;

def spellCheck(refDict, sampleDict):
    'Cross-checks the sample and ref files and outputs a dict of misspelled words'
    
    refList = []
    sampleList = []
    
    #Inserts words in the refDict into a list
    for ref in refDict:
        refList.append(ref)
        
    #Inserts words in the sampleDict into a list
    for word in sampleDict:
        sampleList.append(word)
    
    #Removes digits
    for word in sampleList:
        if (str.isdigit(word)):
            sampleList.remove(word)
    
    #Prints all the misspelled
    for word in sampleList:
        if((word in (w for i, w in enumerate(refList) if i != 1)) == False):
            print ('Misspelled the word \'' + word + '\' ' + str(sampleDict[word]) + ' time(s)')

def checkFrequency(sampleDict):
    'Returns number of times word has been used in sample file'
    
    #Loops through the while loop until an empty string is entered
    while True:
        word = input('\nPlease enter the word to get word count. \nYou can also enter an empty string to terminate the application: \n').lower()
        if(word == ''):
            print('Operation terminated. Thanks for using SpellCheck.')
            break
        if(word in sampleDict):
            print('The word \'' + word + '\' is repeated ' + str(sampleDict[word]) + ' times')
        else:
            print('The word \'' + word + '\' is not present in the sample file. Please try again.')
            continue

def main():
    'Main function of program'
    
    #Gets the ref file
    refFile = getInputDescriptor(False)
    refDict = readFrequency(refFile)
    refFile.close();
    
    #Gets the sample file
    sampleFile = getInputDescriptor(True)
    sampleDict = readFrequency(sampleFile)
    sampleFile.close();
    
    #Spellchecks
    spellCheck(refDict, sampleDict)
    
    #Prompts user for word usage
    checkFrequency(sampleDict)
#main

main()
