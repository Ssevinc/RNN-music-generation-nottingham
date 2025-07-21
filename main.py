from dataset_prep import load_all_tunes
import random
from sklearn.model_selection import train_test_split
import numpy as np

all_tunes = load_all_tunes()

train_tunes,test_tunes = train_test_split(
    all_tunes, test_size=0.1,random_state=42)

print(train_tunes[0])
#A single string with all the the training tunes included.
songs_joined = "\n\n".join(train_tunes)

# Creates the vocablary by finding all the unique characters
vocab = sorted(set(songs_joined))

#vectorize the text based tunes

char2idx = {u: i for i, u in enumerate(vocab)}

idx2char = np.array(vocab)

print(char2idx)


