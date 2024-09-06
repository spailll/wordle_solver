import json
import numpy as np

def get_word_list(file_path="./words.json"):
    with open(file_path, 'r') as file:
        data = json.load(file)
        words_array = [entry['word'] for entry in data]
    return words_array

