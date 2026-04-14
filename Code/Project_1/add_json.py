import os

# oneDNN warning band karne ke liye
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

# extra TensorFlow warnings hide karne ke liye
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import json
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, GlobalAveragePooling1D
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder

with open("Quick.json") as file:
    data = json.load(file)
print(data)
