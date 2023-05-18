import numpy as np
import pandas as pd
from pandas_datareader import data
import yfinance as yf
from datetime import datetime
import yfinance as yf

tickers =['AAME','AAPL','ABNB','ACB','ACLS','ADES','AIO','APD','BCX','BOCN','AMZN','META','TSLA','F','MSFT','CNHI','CNXN','EAR','EBAY','ECBK','ECC','NKE','ELSE','FOSL','FTI','GDOT','GES','GILT','GM','GTIM','HTOO','ADS','AMP','PIRC','VLS','VOW3','RAT','RACE','FDA','BION'] 
dataframes=[]
inizio = datetime(2012,9,15)
fine = datetime.today()

for tick in tickers:
    data = yf.download(tick, inizio, fine, interval='1d')
    data=data.assign(Ticket=f"{tick}")
    dataframes.append(data)
dataframes=pd.concat(dataframes)
print(dataframes)
#dataframes.to_csv("storici.csv")


