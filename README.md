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
- RNN model (implemented essentially using PyTorch)

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
