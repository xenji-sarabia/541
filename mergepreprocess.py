import winsound
import pandas as pd

def playsound():
    winsound.PlaySound('ding.mp3', winsound.SND_FILENAME)

def main():
    try:
        path='megakevin_4.csv'
        chunky=200000
        df=pd.DataFrame()
        for chunk in pd.read_csv(path,chunksize=chunky):
            df=df.append(chunk,ignore_index=True)
        
        df=df.drop(columns=['Unnamed: 0.1.1'])
        df['business_id']=df['business_id'].astype('str')
        #df=df['is_open'].astype('bool')
        print(df.dtypes)
        print(df)
        #print(df.loc[24,'attributes'])
        df.to_csv("megakevin_5.csv",index=False)
        playsound()
    except:
        playsound()
if __name__ == '__main__':

  main()