from pathlib import Path
import random
from music21 import converter
import os
from sklearn.model_selection import train_test_split


def split_abc_file(text):
    """
    splits the ABC text files that we have into individual tunes.
    Each tune starts with a line that begins with 'X:'
    """
    lines = text.splitlines()
    tunes = []
    current = []
    for line in lines:
        if line.strip().startswith("X:"):
            if len(current) > 0:
                tunes.append("\n".join(current))
                current = []
        current.append(line)
    if len(current)>0:
        tunes.append("\n".join(current))
    return tunes

def load_all_tunes():
    all_tunes = []
    data_folder = Path("dataset")
    for file in data_folder.glob("*.abc"):
        abc_text = file.read_text(encoding = "utf-8")
        tunes = split_abc_file(abc_text)
        all_tunes.extend(tunes)
    return all_tunes

#Converting an abc to a wav audio file for format check
if __name__ == "__main__":
    the_tunes = load_all_tunes()
    abc = random.choice(the_tunes)
    score = converter.parse(abc, format = 'abc')
    score.write('midi', fp='test.mid')
    os.system("/Users/s.sevinc/musicgen-nottingham/dataset/FluidR3_GM.sf2") #replace it with path to the file FluidR3_GM.sf2
    os.remove("test.wav")
