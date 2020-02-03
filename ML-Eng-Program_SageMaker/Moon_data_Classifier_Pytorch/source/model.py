import torch
import torch.nn as nn
import torch.nn.functional as F

## TODO: Complete this classifier
class SimpleNet(nn.Module):
    
    ## TODO: Define the init function
    def __init__(self, input_dim, hidden_dim, output_dim):
        '''Defines layers of a neural network.
           :param input_dim: Number of input features
           :param hidden_dim: Size of hidden layer(s)
           :param output_dim: Number of outputs
         '''
        super(SimpleNet, self).__init__()
        
        # two linear layers
        self.fc1 = nn.Linear(input_dim,hidden_dim)
        self.fc2 = nn.Linear(hidden_dim,output_dim)
        #dropout layer p = 0.25
        # dropout prevents overfittinh of data
        self.dropout = nn.Dropout(0.25)
        # sigmoid layer
        self.sig = nn.Sigmoid()
        

    ## TODO: Define the feedforward behavior of the network
    def forward(self, x):
        '''Feedforward behavior of the net.
           :param x: A batch of input features
           :return: A single, sigmoid activated value
         '''
        out = F.relu(self.fc1(x)) # activation and hidden layer
        out = self.dropout(out)
        out = self.fc2(out)      
        
        
        
        return self.sig(out) # return class score