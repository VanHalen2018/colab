# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

import pandas as pd 
import numpy as np

filename_ = "https://raw.githubusercontent.com/2blam/ML/master/deep_learning/Churn_Modelling.csv"

def getdata(fname = filename_):
    temp = pd.read_csv(fname, index_col=0)
    return temp
    
    
