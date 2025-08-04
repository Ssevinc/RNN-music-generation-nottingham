# Music Generation with ABC Notation

This project trains a character-level RNN to generate music in ABC notation using the Nottingham dataset.

## Overview

- A collection of over 600 traditional tunes is used to teach a neural network to compose music.
- The model learns musical patterns character by character.
- Generated outputs are saved in both ABC and audio (`.wav`) formats.

## Features

- **ABC File Preprocessing**: Custom logic to parse and structure musical data
- **Train/Test Split**: Ensure model generalization
- **Vocabulary Encoding**: Convert characters into vectorized sequences
- **Audio Generation**: Convert ABC → MIDI → WAV using `music21` and `fluidsynth`

## Dataset

- **Source**: [Nottingham Music Database](http://abc.sourceforge.net/NMD/)
- **Format**: ABC Notation
- **Number of Songs Used**: 678+
- **Structure**: Each song starts with a line beginning with `X:`

## Used;

- Python
- `music21`, `fluidsynth` – symbolic-to-audio conversion
- `scikit-learn`, `NumPy` – data processing
- RNN model (implemented using PyTorch)

## Model;
 - Type: LSTM (Recurrent Neural Network)
 - Embedding Dim: 256
 - Hidden Size: 512
 - Training Epochs: 10
 - Batch Size: 16
 - Sequence Length: 50
 - Loss Function: CrossEntropyLoss
 - Optimizer: Adam (lr = 0.0005)

## Results;
 - Final training loss: ~0.52
 - Generated pieces range from 15 to 45 seconds, depending on the number of predicted tokens and their rhythmic content.
 - ABC output is converted into .mid and then .wav using abc2midi and fluidsynth.

## Limitations;
 - Repetition in outputs: Introduce temperature sampling to control randomness and avoid loops.
 - Single-layer LSTM: Try multi-layer LSTM or GRU for improved memory.
 - Character-level modeling: Move toward token-level modeling (notes, durations, etc.).

## Credits

This project is inspired by and builds upon materials from the [MIT 6.S191: Introduction to Deep Learning](http://introtodeeplearning.com) course.  
Original labs are released under the MIT License and can be found [here](https://github.com/aamini/introtodeeplearning).

Modifications, additions, and extensions are my own.

## Getting Started

```bash
git clone https://github.com/Ssevinc/RNN-music-generation-nottingham
cd musicgen-nottingham
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
