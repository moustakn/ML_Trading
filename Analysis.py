import pandas as pd
import matplotlib.pyplot as plt

def test_run():
    df = pd.read_csv("Data/HCP.csv")

    #Three ways to print Data from the file
    #print(df.tail(n=10)) #Last 10 lines
    #print(df.head())     #First 5 lines
    #print(df)            #Whole File

    print(df[5:10])        #Slice from 5-9


def get_max_close(symbol):
    '''Return the maxium closign value for a stock indicated by symbol'''

    df = pd.read_csv("Data/{}.csv".format(symbol))  #Reads in data and accepts an arg to determine which file
    return df['Close'].max()                        #Compute and return max from close column

def test_run_close():

    for symbol in ['APPL','HCP']:
        print("Max Close")
        print(symbol,get_max_close(symbol))

def test_run_matlib():

    df = pd.read_csv("Data/APPL.csv")
    print(df['Adj Close'])
    df['Adj Close'].plot()
    plt.show()                  #Must be called to show plots

if __name__ == "__main__":
    #test_run()
    #test_run_close()
    test_run_matlib()

    #compute 0:27ls