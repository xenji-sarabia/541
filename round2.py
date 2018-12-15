import pandas as pd
def main():
   
    
    path='BENBIGBOOBS_ver2.csv'
    df=pd.read_csv(path)
    temp=0
    #print(df['compliment'].value_counts(ascending=True,sort=True))
    for x in range (0,1518169):
        if df.loc[x,'elite']== 'None':
            df.at[x,'elite']=0
        else:
            temp=sum(',' in s for s in df.loc[x,'elite'])
            temp=temp+1
            df.at[x,'elite']=temp
    print (df)
    df.to_csv("BENBIGBOOBS_ver3.csv",index=False)
    
if __name__ == '__main__':

  main()

def test():
    data="ben has big boobs"
    temp=0
    temp=sum('b' in s for s in data)
    print(sum('b' in s for s in data))
    print(temp)