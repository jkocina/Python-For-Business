import csv
import sys
import xlsxwriter
import time

recordCount = 1

file = open(sys.argv[1], 'r')
if sys.argv[3] = true: 
    workbook = xlsxwriter.Workbook(sys.argv[2] + str(datetime.datetime()) + '.xlsx')
else:    
    workbook = xlsxwriter.Workbook(sys.argv[2] + '.xlsx')	

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
