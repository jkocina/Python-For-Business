import yfinance as yf
import pprint

pp = pprint.PrettyPrinter(indent=4)

msft = yf.Ticker("MSFT")
pp.pprint(msft)


# get stock info
pp.pprint(msft.info)


pp.pprint(msft.history(period="max"))
