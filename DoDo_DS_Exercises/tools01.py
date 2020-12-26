# Tools for DoDo DS exercises
# Write Python 3 code in this online editor and run it.

import pandas as pd 
import numpy as np

filename_ = "https://raw.githubusercontent.com/2blam/ML/master/deep_learning/Churn_Modelling.csv"

# gat data

def getdata(fname = filename_):
    '''
    read the csv formated data from web
    param fname: file name and html address - default filename_
    index is the first column
    return dataframe
    '''
    temp = pd.read_csv(fname, index_col=0)
    return temp

# generate n "bad lines"
    
ms_lines_ = 20
def missing_lines(df, columns, n = ms_lines_):
  '''
  Creates n "bad rows" in the database
  param df: dataframe
  param columns: list of the bad columns in the datafarme - default ms_lines_
  param n: count of the bad rows
  '''
  missing_index = np.random.randint(len(df), size=n)
  df.loc[missing_index, columns] = np.nan
  return df

# scattered errors in the database

def test_data(df, holes):
  '''
  places n holes in the database.
  the data in the first two columns do not change.
  param df: dataframe
  param holes: count of missing values
  return temp dataframe
  '''
  rows = len(df)
  cols = len(df.columns)
  mask = np.full((rows,cols),False)  

  for i in range(40):
    row = rnd.randint(0,rows)
    col = rnd.randint(2,cols-1)
    mask[row,col] = True  

  temp = np.where(mask,np.nan, df)
  temp = pd.DataFrame(temp, index=df.index, columns=df.columns)
  print(temp.isna().sum())

  return temp
