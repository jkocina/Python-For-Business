# Python program to convert text 
# file to JSON 
  
  
import json 


def textToJson():
    
    # the file to be converted 
    tickersLocation = 'NYSE.txt'
    
    # intermediate and resultant dictionaries 
    # intermediate 
    dict2 = {} 
    
    # resultant 
    dict1 = {} 
    
    # fields in the sample file  
    fields =['symbol', 'description'] 
    
    with open(tickersLocation) as tickers: 
        
        # loop variable 
        i = 0
        
        # count variable for ticker  
        l = 1
        
        for ticker in tickers: 
            
            # reading line by line from the text file 
            tickerNoNewLine = ticker.split('\n')
            
            tickerText = list(tickerNoNewLine[0].split('\t'))
           #print(tickerText[0]) 
            
            # for automatic creation of id for each employee 
            #sno ='T'+str(l) 
        
            dict2.update({[fields[0]] : tickerText[0], fields[1] : tickerText[1]})

            # while i<len(fields): 
                
            #     # creating dictionary for each employee 
                
            #     if i == 0:
                    
            #         dict2.update([fields[i]] : tickerText[0] , 
            #     else:

            #         dict2[l][fields[i]] = tickerText[1]    

            #     i = i + 1

            #print(dict2)       
            # appending the record of each employee to 
            # the main dictionary 
            dict1.update(dict2)
            l = l + 1
            i = 0

    #print(dict1)
    print(dict2)    
    # creating json file         
    # out_file = open("tickers.json", "w") 
    # json.dump(dict1, out_file, indent = 4) 
    # out_file.close()


def htmlToJSON():
    # import html

    # use dom to find table root

    # iterate through the table headers and save those in one array

    # interate through each one of the records and data points putting them under the right heading


    # for each tableHeader
    #     headerArray += tableHeader

    
    # for each Record
        
    #     let r = 0
        
    #     for each tableheader

    #         for each dataPoint

    #         completeArray[r][tableheader] = dataPoint
        
        
    #     r = r + 1


textToJson()