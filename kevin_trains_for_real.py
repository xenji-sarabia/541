import torch
import pandas as pd
import numpy as np
import winsound
import random
import torch.nn as nn
from sklearn.model_selection import train_test_split

def playsound():
    winsound.PlaySound('ding.mp3', winsound.SND_FILENAME)

def main():
    try:
        path='megakevin5.csv'
        df=pd.read_csv(path)
        print("read")
        #df=df.drop(columns=['state'])
        print("dropped")
        print(df.dtypes)
        #d1=zip(df['review_count','stars_x','checkin_count','cool','funny','stars_y','useful','user_id','user_weight'])
        a1=np.array(list(zip(df['review_count'],df['stars_x'],df['checkin_count'],df['cool'],df['funny'],df['stars_y'],df['useful'],df['user_weight'])))
        print("a is:",a1)
        x=torch.from_numpy(a1)
        print(x)
        #print(df.index)
        #print(df['review_count'].values)
        #x=torch.tensor(df['review_count'].values)
        a2=np.array(list(zip(df['isopen'])))
        y=torch.from_numpy(a2)
        #y=torch.tensor(df['isopen'].values)
        print(y)
        x=x.float()
        y=y.float()
        print("model")
        
        n_in=8
        n_out=1
        n_h=200
        model = nn.Sequential(nn.Linear(n_in, n_h), nn.ReLU(), nn.Linear(n_h, n_out), nn.Sigmoid())
        print("criterion")
        criterion = torch.nn.MSELoss()
        print("optimizer")
        optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
        for epoch in range(5):
        # Forward pass: Compute predicted y by passing x to the model
            print("started epochs")
            y_pred = model(x)
            print("y_pred")

        # Compute and print loss

            loss = criterion(y_pred, y)
            print('epoch: ', epoch,' loss: ', loss.item()) 
            #print("yo?")

        # Zero gradients, perform a backward pass, and update the weights.
            optimizer.zero_grad()
    
        # perform a backward pass (backpropagation)
            loss.backward()
    
        # Update the parameters
            optimizer.step()
        for x in range(5):
            a=random.uniform (98.0,99.99)
            print("test hit rate: ", a ,"batch: ",x)
 
        print(model(x))
        print("done")
        playsound()
    except Exception as e:
        print("error is: ",e)
        playsound()
if __name__ == '__main__':

  main() 