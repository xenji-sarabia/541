import pandas as pd 
import numpy as np

def main():
    path='chrisdata_csv2.csv'
    df=pd.read_csv(path)
    temp=0
    '''for x in range (0, 1518169):
        if df.loc[x,'elite']==0 and temp<df.loc[x,'misc_score'] :
            temp=df.loc[x,'misc_score']
            print(df.loc[x])
    
    
    '''
    print(df)

if __name__ == '__main__':

  main()