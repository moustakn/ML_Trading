import os
import pandas as pd
import matplotlib.pyplot as plt

def read_data():
    '''Basic displaying of data'''
    df = pd.read_csv("Data/HCP.csv")

    #Three ways to print Data from the file
    print(df.tail(n=10))   #Last 10 lines
    print(df.head())       #First 5 lines
    print(df)              #Whole File

    print(df[5:10])        #Slice from 5-9


def get_max_close(symbol):
    '''Return the maxium closign value for a stock indicated by symbol'''

    df = pd.read_csv("Data/{}.csv".format(symbol))  #Reads in data and accepts an arg to determine which file
    return df['Close'].max()                        #Compute and return max from close column

def show_close_price():
    '''Passes a string to determine which file to use'''

    for symbol in ['APPL','HCP']:           #Loop over two stings
        print("Max Close")
        print(symbol,get_max_close(symbol)) #Prints the symbol and passes it into the get_max_close function

def use_matlib_to_plot():
    '''Plotting multiple columns'''

    df = pd.read_csv("Data/APPL.csv")
    print(df[['High','Close','Low']])
    df[['High','Close','Low']].plot()    #Plots multiple columns on the chart
    plt.show()                           #Must be called to show plots

def date_range():
    '''Constructing a dataframe in pandas based on a date range'''

    start_date='2017-01-10'                 #Define a date range
    end_date='2017-01-22'
    dates=pd.date_range(start_date,end_date)

    df1 = pd.DataFrame(index=dates)         #Create an empty dataframe
    dfSPY = pd.read_csv("Data/SPY.csv",index_col="Date",parse_dates=True,
                        usecols=['Date','Adj Close'], na_values=['NaN'])
                                            #Read SPY data using the Date column as the index column for the join
                                            #Only retrive two columns and define NaN as not a number

    dfSPY = dfSPY.rename(columns={'Adj Close':'SPY'})
                                            #Rename the df to avoid a clash in column names
    df1=df1.join(dfSPY,how='inner')         #Join the two dataframes and define an inner join
    df1 = df1.dropna()                      #Drop the NaN values


    '''This for loops reads data from each symbols csv file and joins it to the SPY df'''
    symbols = ['APPL','HCP','IBM']
    for symbol in symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol), index_col='Date',parse_dates=True,
                            usecols=['Date','Adj Close'], na_values=['NaN'])

                                #Note I used symbol_to_path to get the symbol related to the path
                                #Instead of doing read_csv(/"Data/{}.csv/".format(symbol))

        df_temp = df_temp.rename(columns={'Adj Close':symbol})
        df1 = df1.join(df_temp)

    print(df1)

def symbol_to_path(symbol, base_dir="Data"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))


if __name__ == "__main__":
    #read_data()
    #show_close_price()
    #use_matlib_to_plot()
    date_range()
