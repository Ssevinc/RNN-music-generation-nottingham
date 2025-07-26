import random
from sklearn.model_selection import train_test_split
import numpy as np
from preprocess import Preprocess
import torch

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

