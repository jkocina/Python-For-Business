import csv
import sys
import xlsxwriter
import time

recordCount = 1

file = open(sys.argv[1], 'r')
	
chooseExcelFileName(sys.argv[2], sys.argv[3])

worksheet = workbook.add_worksheet()

try:
    reader = csv.reader(file)
    for row in reader:
        print("Record Count: " + str(recordCount))
	    columnCount = "A"
		
	    for dataPoint in row:
	        #print(dataPoint)
		worksheet.write(columnCount + str(recordCount), dataPoint)
		columnCount = chr(ord(columnCount) + 1)
	    recordCount += 1
	
finally:
	file.close()	
workbook.close()

def chooseExcelFileName(name, timeStamp):
    if name != 0:
        if timeStamp = true: 
            workbook = xlsxwriter.Workbook(name + str(datetime.datetime()) + '.xlsx')
        else:    
            workbook = xlsxwriter.Workbook(name + '.xlsx')	
    else: 
        if timeStamp = true: 
            workbook = xlsxwriter.Workbook(newFile + str(datetime.datetime()) + '.xlsx')
        else:    
            workbook = xlsxwriter.Workbook(newFile + '.xlsx')    
