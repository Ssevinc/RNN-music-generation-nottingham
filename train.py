import torch
from model import LSTMModel
from preprocess import Preprocess
import torch.optim as optim
import torch.nn as nn
from utils import Logger


hyperparams = {
    "embedding_dim": 256,
    "hidden_size": 512,
    "seq_length": 50,
    "batch_size": 16,
    "num_epochs": 10,
    "learning_rate": 0.0005
}

logger = Logger(log_dir="logs", experiment_name="nottingham_rnn", params=hyperparams)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
prep = Preprocess()

input_batches, target_batches = prep.create_batches(
    seq_length=hyperparams["seq_length"],
    batch_size=hyperparams["batch_size"]
)

x = torch.tensor(input_batches, dtype=torch.long)
y = torch.tensor(target_batches, dtype=torch.long)

vocab_size = len(prep.vocab)
model = LSTMModel(vocab_size,hyperparams["embedding_dim"], hyperparams["hidden_size"]).to(device)
optimizer = optim.Adam(model.parameters(), lr=hyperparams["learning_rate"])
criterion = nn.CrossEntropyLoss()

model.train()

for epoch in range (hyperparams["num_epochs"]):
    state = None
    total_loss = 0

    for i in range(len(x)):
        x_batch = x[i].unsqueeze(0).to(device)
        y_batch = y[i].unsqueeze(0).to(device)

        optimizer.zero_grad()
        pred, state = model(x_batch, state, return_state=True)

        state = tuple([s.detach() for s in state])
        loss = criterion(pred.view(-1, vocab_size), y_batch.view(-1))

        loss.backward()
        optimizer.step()

        total_loss += loss.item()

        if (i + 1) % 100 == 0:
            print(f"Epoch [{epoch+1}/{hyperparams['num_epochs']}], Step [{i+1}/{len(x)}], Loss: {loss.item():.4f}")


    avg_loss = total_loss / len(x)
    print(f"\nEpoch [{epoch+1}] completed. Average Loss: {avg_loss:.4f}\n")
    logger.log_metrics(epochs=epoch+1,train_loss=avg_loss)

logger.save()
torch.save(model.state_dict(), "trained_model.pt")



