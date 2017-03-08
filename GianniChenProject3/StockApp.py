'''
Created on Apr 18, 2016

@author: Gianni
'''
def getInputDescriptor():
        
    while True:
        try:
            inputFileName = input('Please input the name of the input file: \n')
            inFile = open(inputFileName, 'r')
        except OSError:
            print("You entered an invalid name. Please try again.")
            continue
        else:
            break
        
    return inFile

def getDataList(file_object, column_number):
    
    returnList = []
    masterList = []
    dateList = []
    valueList = []
    
    file_object.readline()
    masterList = file_object.readlines()
    for n in masterList:
        dateList.append(n.split(',')[0])
        valueList.append(n.split(',')[column_number])
        
    returnList = list(zip(dateList, valueList))
    return returnList

def averageData(list_of_tuples):

    monthYearList = []
    valList = []
    dateValList = []
    returnDate = []
    returnVal = []
    returnList = []
    total = 0.00
    count = 0
    
    for n in list_of_tuples:
        date, val = n
        monthStr = (date.split('-')[1])
        yearStr = (date.split('-')[0])
        monthYearList.append(monthStr + ':' + yearStr)
        valList.append(val)
    
    dateValList = list(zip(monthYearList, valList))
    
    out, value = dateValList[0]
    for element in dateValList:
        comp, value = element
        floatVal = float(value)
        if (out == comp):
            total += floatVal
            count += 1
        else:
            returnDate.append(out)
            returnVal.append(total/count)
            out = comp
            total = floatVal
            count = 1
    returnDate.append(out)
    returnVal.append(total/count)
    
    returnList = list(zip(returnDate, returnVal))
    return (returnList)
    
def outputAverage(filename, average):
    
    outfile = open(filename, 'w')
    for n in average:
        outfile.write('{0}{1:15.2f}\n'.format(n[0],n[1]))
    outfile.close()
    
def main():
    
    inFile = getInputDescriptor()
    for n in range(1,7):
        averageList = averageData(getDataList(inFile, n))
        outFileName = 'data_' + str(n) +'.txt'
        outputAverage(outFileName, averageList)
        'Reset Cursor'
        inFile.seek(0)
    inFile.close()

#Main Part
main()