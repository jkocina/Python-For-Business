# Python script to convert a txt doc of stock tickers to json
# file to JSON
import json
import pprint
from xml.dom.minidom import parse, parseString

pp = pprint.PrettyPrinter(indent = 4)

def textToJson():

    # the file to be converted
    tickersLocation = 'NYSE.txt'

    # data dictionary to to populate and convert to json
    dict2 = {}

    # fields in the sample file
    fields =['symbol', 'description']

    #opening the tickers file
    with open(tickersLocation) as tickers:

        # loop variable
        i = 0

        # count variable for ticker
        l = 1

        # reading line by line from the text file
        for ticker in tickers:

            #removing the new line at the end of each Line
            tickerNoNewLine = ticker.split('\n')

            #spliting symbol and description
            tickerText = list(tickerNoNewLine[0].split('\t'))

            #trying this to avoid index errors from the data dictionary when the descripiton is empty
            try:
                dict2[l] = {fields[0] : tickerText[0], fields[1] : tickerText[1]}
            except:

                dict2[l] = {fields[0] : tickerText[0]}

            l = l + 1


    #printing out the dictionary
    pp.pprint(dict2)

    # creating and populating the json file
    out_file = open("tickers.json", "w")
    json.dump(dict2, out_file, indent = 4)
    out_file.close()


#def htmlToJSON():
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
