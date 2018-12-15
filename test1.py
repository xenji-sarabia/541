import winsound
import pandas as pd
import numpy as np

def playsound():
    winsound.PlaySound('ding.mp3', winsound.SND_FILENAME)

def main():
    try:
        a = [['a', '1.2', '4.2'], ['b', '70', '0.03'], ['x', '5', '0']]
        df = pd.DataFrame(a, columns=['one', 'two', 'three'])
       # print(df)
        #print(df.dtypes)
        '''ser=pd.Series([1,2],dtype='int 32')
        print(ser)
        print(ser.dtype)
        ser.astype('int64')
        print(ser)
        print(ser.dtype)
        '''
        print(df['three'])

        df['three']=df['three'].astype('str')
        print("dickface")
        print(df)
        print(df.dtypes)

        x=13
        print("x is: ",x)

        playsound()
    except:
        playsound()
if __name__ == '__main__':

  main()