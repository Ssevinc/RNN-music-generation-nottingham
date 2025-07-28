import torch
from model import LSTMModel
from preprocess import Preprocess
import torch.optim as optim


embedding_dim = 256
hidden_size = 1024
batch_size = 8
seq_length = 100
num_epochs = 20

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
prep = Preprocess()


