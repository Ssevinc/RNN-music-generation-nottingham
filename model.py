import torch
import torch.nn as nn
import torch.optim as optim
#The RNN Model

class LSTMModel(nn.Module):
    def __init__(self, vocab_size,embedding_dim,hidden_size):
        super(LSTMModel,self).__init__()
        super.hidden_size = hidden_size
        self.embedding = nn.Embedding(vocab_size,embedding_dim)

        self.lstm = nn.LSTM(embedding_dim,hidden_size,batch_first=True)

        self.fc = nn.Linear(hidden_size,vocab_size)

    def init_hidden(self,batch_size,device):
        return (torch.zeros(1,batch_size,self.hidden_size).to(device),
                torch.zeros(1,batch_size,self.hidden_size).to(device))
    
    def forward(self,x, state=None, return_state=False):
        x = self.embedding(x)

        if state is None:
            state = self.init_hidden(x.size(0), x.device)
        out, state = self.lstm(x, state)

        out = self.fc(out)

        return out if not return_state else (out,state)
                




