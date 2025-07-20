from one_file import load_all_tunes
import random
from sklearn.model_selection import train_test_split

all_tunes = load_all_tunes()

train_tunes,test_tunes = train_test_split(
    all_tunes, test_size=0.1,random_state=42)

