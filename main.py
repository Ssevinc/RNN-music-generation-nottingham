import random
from sklearn.model_selection import train_test_split
import numpy as np
from preprocess import Preprocess
import torch
import torch.nn as nn
import torch.optim as optim
from model import LSTMModel


prep = Preprocess()

#test vectorized data
vectorized = prep.vectorized_data
print("Sample vectorized data:", vectorized[:10])

#create batches (numpy arrays)
input_batches,target_batches = prep.create_batches(seq_length=10,batch_size=2)

assert len(input_batches) == len(target_batches)
assert all(len(seq) == 10 for seq in input_batches)
assert all(len(seq) == 10 for seq in target_batches)

x_batch = torch.tensor(np.array(input_batches), dtype=torch.long)
y_batch = torch.tensor(np.array(target_batches), dtype=torch.long)

print("x_batch shape:", x_batch.shape)  # should be [batch_size, seq_length]
print("y_batch shape:", y_batch.shape)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
x_batch = x_batch.to(device)
y_batch = y_batch.to(device)

vocab_size = len(prep.vocab)
model = LSTMModel(vocab_size,256,1024).to(device)

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

for epoch in range(10):
    model.train()
    optimizer.zero_grad()
    

