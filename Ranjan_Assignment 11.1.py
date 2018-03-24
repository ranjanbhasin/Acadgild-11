# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 21:08:00 2018

@author: Ranjan
"""
#import pandas package
import pandas as pd

# pre-defined dataframe as per exercise given
df = pd.DataFrame({'X': [7, 2, 0, 3, 4, 2, 5, 0, 3, 4]})

#initialize variables (including for new col)
closer=0
Y=[]

#using for loop to iterate

for i in range(len(df["X"])):

    #condition if value is 0
    if df["X"][i]==0:
        closer=0
        Y.append(0)
    #condition if value is not 0
    else:
        closer+=1
        Y.append(closer)

#adding the list of values (closer) within the data frame        
df["Y"]=Y

  #printing the dataframe
print(df)
        