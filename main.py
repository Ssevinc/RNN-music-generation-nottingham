import random
from sklearn.model_selection import train_test_split
import numpy as np
from preprocess import Preprocess
"""
all_tunes = load_all_tunes()
train_tunes,test_tunes = split_dataset()

songs_joined = "\n\n".join(train_tunes)

vocab = sorted(set(songs_joined))

char2idx = {u: i for i, u in enumerate(vocab)}
idx2char = np.array(vocab)

def vectorize(string):
    vectorized = ([char2idx[char] for char in string])
    return vectorized

vectorize(songs_joined)
"""

prep = Preprocess()
input_batches,target_batches = prep.create_batches(seq_length=10,batch_size=2)
print("Input example:", input_batches[0][0])
print("Target example:", target_batches[0][0])