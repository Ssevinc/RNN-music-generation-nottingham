from dataset_prep import load_all_tunes,split_dataset
import random
import numpy as np

all_tunes = load_all_tunes()

class Preprocess:
    def __init__(self):
        self.train_tunes, self.test_tunes = split_dataset()
        self.songs_joined = "n\n".join(self.train_tunes)
        self.vocab = sorted(set(self.songs_joined))
        self.char2idx = {u: i for i, u in enumerate(self.vocab)}
        self.idx2char = np.array(self.vocab)
        self.vectorized_data = self.vectorize(self.songs_joined)

    def vectorize(self,string):
        return np.array([self.char2idx[char] for char in string])
    
    def create_batches(self,seq_length,batch_size):
        self.seq_length = seq_length
        self.batch_size = batch_size
        num_sequences = len(self.vectorized_data)// (seq_length+1)    
        usable_data =  self.vectorized_data[:num_sequences*(seq_length+1)]
        sequence = usable_data.reshape((num_sequences, seq_length+1))
        inputs = sequence[:,:-1]
        targets = sequence[:,1:]

        num_batches = num_sequences// batch_size
        inputs= inputs[:num_batches*batch_size]
        targets = targets[:num_batches*batch_size]

        input_batches = inputs.reshape((num_batches,batch_size,seq_length))
        target_batches = targets.reshape((num_batches,batch_size, seq_length))

        return input_batches,target_batches
    

