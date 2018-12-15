import torch
import pandas as pd
import winsound
import numpy as np
import torch.nn as nn

def playsound():
    winsound.PlaySound('ding.mp3', winsound.SND_FILENAME)

def main():
    try:

        if torch.cuda.is_available():
            print("its on")
        #path='megakevin2.csv'
        #df=pd.read_csv(path)
        
        d={'A':[1.0,2,4],'B':[3,6,9],'C':[5,6,7]}
        '''
        d1=pd.DataFrame(data=d)
        print(d1)
        d2=pd.DataFrame(data=d1['A'])
        print("d2\n",d2)
        d3=pd.DataFrame(data=d) 
        print("d3\n",d3)  
        d4=pd.merge(d2,d3[['B']])
        print("d4,\n",d4)
        '''
        d1=pd.DataFrame(data=d)
        d2=zip(d1['A'],d1['B'])
        
        #d1['x'].flatten()
        #print("d1x\n",d1['x'])
        print(list(d2))
        a1=np.array(list(zip(d1['A'],d1['B'])))
        print(a1)
        a=torch.from_numpy(a1)
        a.type(torch.FloatTensor)
        print(a)
        print("merged \n",d1)
        '''print(d1)
        print(d1['A'])
        print(d1)
        print(torch.tensor(d1['A']))
        x=torch.tensor(d1['A'])
        print(x)
        
        df=pd.DataFrame(data=d1)
        #df=df.transpose
        print(df)
        #print(df.dtypes)
        #x=torch.cuda.tensor(df['review_count','stars_x','checkin_count','cool','funny','stars_y','useful','user_weight'].values,dtype=torch.float)
        print("barrier")
        #print(df['A'])
        x=torch.cuda.FloatTensor(df['A'].values)
        y=torch.cuda.FloatTensor(df['B'])
        print(x.size())
        #n_in=1
        #n_out=1
        #n_h=5
        #batch_size=1
        print(df['A'].size)
        print(x)
        print(torch.randn(1, 2))
        '''
        '''
        n_in is number of variables per instance
        
        '''
        #NN = Neural_Network()
        '''for i in range(1000):  # trains the NN 1,000 times
            print ("#" + str(i) + " Loss: " + str(torch.mean((y - NN(x))**2).detach().item()))  # mean sum squared loss
            NN.train(x, y)
            NN.saveWeights(NN)
            NN.predict()
        '''
        '''
        n_in, n_h, n_out, batch_size = 2, 5, 1, 10
        #n_in=length

        #x=torch.cuda.tensor(df['user_weight'].values)
        x = torch.randn(batch_size, n_in)
        print(x)
        x=torch.tensor([[1.0,2.0],[3.0,4.0],[5.0,6.0],[7.0,8.0],[9.0,10.0],[11.0,12.0],[13.0,14.0],[15.0,16.0],[17.0,18.0],[19.0,20.0]])
        y = torch.tensor([[3.0], [7.0], [11.0], [15.0], [19.0], [23.0], [27.0], [31.0], [35.0], [39.0]])
        #y=torch.cuda.tensor(df['is_open'].values)
        print(x)
        print("model")
        model = nn.Sequential(nn.Linear(n_in, n_h), nn.ReLU(), nn.Linear(n_h, n_out), nn.Sigmoid())
        print("criterion")
        criterion = torch.nn.MSELoss()
        print("optimizer")
        optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
        for epoch in range(50):
        # Forward pass: Compute predicted y by passing x to the model
            
            y_pred = model(x)
            #print("y_pred")

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
        '''   
        '''
        '''
        playsound()
    except:
        playsound()
if __name__ == '__main__':

  main()
'''
class Neural_Network(nn.Module):
    
    def __init__(self, ):
        super(Neural_Network, self).__init__()
        # parameters
        # TODO: parameters can be parameterized instead of declaring them here
        self.inputSize = 3
        self.outputSize = 3
        self.hiddenSize = 6

        # weights
        self.W1 = torch.randn(self.inputSize, self.hiddenSize) 
        self.W2 = torch.randn(self.hiddenSize, self.outputSize)

    def forward(self, X):
        self.z = torch.matmul(X, self.W1) 
        self.z2 = self.sigmoid(self.z) # activation function
        self.z3 = torch.matmul(self.z2, self.W2)
        o = self.sigmoid(self.z3) # final activation function
        return o

    def backward(self, X, y, o):
        self.o_error = y - o # error in output
        self.o_delta = self.o_error * self.sigmoidPrime(o) 
        self.z2_error = torch.matmul(self.o_delta, torch.t(self.W2))
        self.z2_delta = self.z2_error * self.sigmoidPrime(self.z2)
        self.W1 += torch.matmul(torch.t(X), self.z2_delta)
        self.W2 += torch.matmul(torch.t(self.z2), self.o_delta)
'''