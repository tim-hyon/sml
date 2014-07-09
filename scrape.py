import urllib2
import csv
from urllib2 import HTTPError

tickers = []
nyse = []
nasdaq = []

with open('tickers.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        if (row[2] == 'NYQ'):
            nyse.append(row[0])
        if (row[2] == 'NMS'):
            nasdaq.append(row[0])
tickers = nyse+nasdaq
tickers.sort()
stock_data = []
for stock in tickers:
    try:
        stock_data.append((stock,urllib2.urlopen('http://ichart.finance.yahoo.com/table.csv?s='+stock+'&d=5&e=9&f=2014&g=d&a=0&b=12&c=1995&ignore=.csv').read()))
        print 'scraping... '+stock
    except HTTPError:
        tickers.remove(stock)
        continue

for i in stock_data:
    print 'saving... '+i[0]
    myFile = open('stockdata/'+i[0]+'.csv', 'w')
    myFile.write(i[1])
    myFile.close()


