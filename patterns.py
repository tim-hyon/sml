import os
import datetime

def main():
    #Change to directory where stock csv data is saved
    rootdir = '/Users/Tim/mlstocks/stockdata/'
    stockdata = {}

    #Start date and end date for data covered by script
    date_start = datetime.date(1995,1,12)
    date_start = datetime.date(2014,6,9)

    #Size of windows the script will look over in days
    window_start = 1
    window_end = 14
    
    #The required day change that needs to be present (positive or negative)
    #in both the open and close of the window for a specific window to count
    #towards the relationship
    daychange = 10

    #Percent of windows that have to pass the daychange before stock A->B is
    #considered a relationship. If no stocks meet this threshold, the script 
    #will return num_backup of the next best relationships
    rel_threshold = 90
    num_backup = 20

    stockdata = readAll(rootdir)
    uniquePairs = []
    count = 0

    for window in range(window_start,window_end+1):
        for stock1 in stockdata:
            for stock2 in stockdata:
                if stock1 is not stock2:

    return (stockdata, uniquePairs)



def percentChange(oprice, cprice):
    return (0.0+cprice-oprice)/oprice

def readAll(rootdir):
    retdict = {}
    for files in os.listdir(rootdir):
        if files.endswith(".csv"):
            f = open(rootdir+files,'r')
            lines = f.readlines()
            f.close()
            retdict[files[:len(files)-4]]=lines
    return retdict




