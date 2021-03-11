# modules
import pandas_datareader as pdr 
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np

# A. Data Preprocessing
# ---------------------

# -1- typical price

def typical_price(df):
  temp = pd.DataFrame()
  temp['Typical'] = np.exp((3*np.log(df.Close) + 2*np.log(df.Open) + np.log(df.High) + np.log(df.Low))/7)
  temp.index = df.index
  return temp

# df['Typical'] = typical_price(df)

# -2- Fibo

def fibo(col, period):
  gr = 1.61803398875
  temp = np.zeros(len(col))
  s = 0
  for i in range(period + 1): 
    temp = temp * gr + col.shift(i) 
    s = s * gr + 1
    # print(s, temp[0])
  temp = temp/s 
  return temp

# features = ['High', 'Low', 'Open', 'Close', 'Typical']
# for col in features:
#   df['Fibo_'+col] = fibo(df[col],7)

# -3- differents in time

def diff_time(col, timestep=1):
  temp = pd.DataFrame()
  temp['dtime'] = np.log(col/col.shift(timestep))
  return temp

# for col in features:
#   c1 = "Fibo_" + col
#   c2 = "Log_" + col
#   df[c2] = diff_time(df[c1],1)

# df['Diff_Log_Typical'] = df['Log_Typical'] - df['Log_Typical'].shift(1)

# -4- log RSI

def logRSI(log,period):
  temp = pd.DataFrame()
  absx  = np.abs(log)
  temp['logRSI'] =log.rolling(window = period).sum()/absx.rolling(window = period).sum()
  return temp

# df['logRSI14'] = logRSI(df.Log_Typical,14)
# df['logRSI28'] = logRSI(df.Log_Typical,28)
# df['logRSI56'] = logRSI(df.Log_Typical,56)

# -5- Williams

def williams(df,period):
  mx = df.High.rolling(window = period).max()
  mi = df.Low.rolling(window = period).min()
  av = (mx + mi)/2
  t = mx-mi
  will = (df.Close - av)/t
  return will

# df['Will14'] = williams(df,14)  

# -6- target

def target(df, period):
  target = np.zeros(len(df))
  d = np.array(df.High-df.Low)
  c = np.array(df.Close)
  XX = []
  XX2 = []
  for i in range(len(df)-period-2):
    x = 0
    x2 = 0
    c0 = c[i+1]
    d0 = d[i+1]
    for j in range(i+2,i+period+2):
      c1 = c[j]
      d1 = d[j]

      if d0*d1 !=0: 
        a = (c1-c0)/np.sqrt(d0*d1)
        a = np.arctan(a)
      elif c1>c0:
        a = np.pi/2
      elif c0<c0:
        a = -np.pi/2
      else: 
        a = 0

      x = x + a 
      x2 = x2 + a*a 

    x = x/period
    x2 = np.sqrt(np.abs(x2-period*x**2)/period)
    XX.append(x)
    XX2.append(x2)
    if x2 !=0: 
      target[i] = np.sin(np.arctan(x/x2))
    elif x >0: 
      target[i]=1
    elif x <0:
      target[i]=-1
  return target, np.array(XX), np.array(XX2)

# df['Target'], XX, XX2 = target(df,10) 

