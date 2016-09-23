
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
import sys


# In[ ]:

def col_sort(x,data_file):
    # read file
    df = pd.read_csv(data_file,sep=' ',header=None)
    df = df.as_matrix()[:,1:]
    col = np.array(df[:,x])
    # sorting 
    col = np.sort(col).T
    # to csv 
    np.savetxt('ans1.txt',col,newline=",")

if __name__ == '__main__':
    #col_index,data_file = raw_input().split(" ")
    col_sort(sys.argv[1] ,sys.argv[2] )






