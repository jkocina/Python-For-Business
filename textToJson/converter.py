# Python script to convert a txt doc of stock tickers to json
# file to JSON
import json
import pprint

pp = pprint.PrettyPrinter(indent = 4)

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

        # reading line by line from the text file
        for ticker in tickers:

            #removing the new line at the end of each Line
            tickerNoNewLine = ticker.split('\n')

            #spliting symbol and description
            tickerText = list(tickerNoNewLine[0].split('\t'))

            try:
                dict2[l] = {fields[0] : tickerText[0], fields[1] : tickerText[1]}
            except:

                dict2[l] = {fields[0] : tickerText[0]}


            # appending the record of each employee to
            # the main dictionary
            #dict1.update(dict2)
            l = l + 1


    #printing out the dictionaries
    #print(dict1)
    pp.pprint(dict2)

    # creating json file
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
