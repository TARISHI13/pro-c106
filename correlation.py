import plotly.express as px
import csv
import numpy as np
def plotfigure(datapath,xvalue,yvalue):
    with open (datapath) as csvfile:
        df = csv.DictReader(csvfile)
        fig = px.scatter(df,x = xvalue,y = yvalue)
        fig.show()

def getdatasource(datapath,xvalue,yvalue):
    xvalue1 = []
    yvalue1 = []
    with open(datapath) as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            xvalue1.append(float(row[xvalue]))
            yvalue1.append(float(row[yvalue]))
    return{'x':xvalue1,'y':yvalue1}

def findcorrelation(datasource):
    correlation = np.corrcoef(datasource['x'],datasource['y'])
    print('correlation between the 2 values is',correlation[0,1])

def setup():
    print('enter the datapath')
    datapath = input()
    print('xvalue = ')
    xvalue = input()
    print('yvalue = ')
    yvalue = input()
    datasource = getdatasource(datapath,xvalue,yvalue)
    findcorrelation(datasource)
    plotfigure(datapath,xvalue,yvalue)

setup()
