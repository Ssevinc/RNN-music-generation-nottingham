import torch
from src.model import LSTMModel
from src.preprocess import Preprocess
import random
import numpy as np

embedding_dim = 256
hidden_size = 512
generate_length = 200
model_path = "trained_model.pt"

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

prep = Preprocess()
stoi = prep.stoi
itos = prep.itos

vocab_size = len(prep.vocab)

model = LSTMModel(vocab_size,embedding_dim,hidden_size).to(device)
model.load_state_dict(torch.load(model_path,map_location=device))
model.eval() # model on evaluation mode not training, just generating

#choosing the first token to start generation
seed = [stoi['X']] if 'X' in stoi else [random.randint(0,vocab_size-1)]

input_seq = torch.tensor(seed,dtype=torch.long).unsqueeze(0).to(device)
generated = seed.copy()
state = None

for _ in range(generate_length):
    out,state= model(input_seq, state, return_state= True)
    out = out[:, -1, :]
    probs = torch.softmax(out, dim=1)
    next_token = torch.multinomial(probs, num_samples=1).item()

    generated.append(next_token)
    input_seq = torch.tensor([[next_token]],dtype=torch.long).to(device)

abc_music = ''.join([itos[i] for i in generated])

print("Generated ABC Music")
print(abc_music)

with open("generated_sample_3.abc", "w") as f:
    f.write(abc_music)






