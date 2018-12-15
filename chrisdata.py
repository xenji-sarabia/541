import pandas as pd
import winsound

def playsound():
    winsound.PlaySound('ding.mp3', winsound.SND_FILENAME)

def main():
    path='chrisdata_csv1.csv'
    chunky=200000
    df=pd.DataFrame()
    
    for chunk in pd.read_csv(path,chunksize=chunky):
        df=df.append(chunk,ignore_index=True)
    df=df.drop(columns=['review_id'])
    print(df.head())
    
    df.to_csv("chrisdata_csv2.csv",index=False)
    
    playsound()
if __name__ == '__main__':

  main()



