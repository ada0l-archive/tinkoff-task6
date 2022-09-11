import os
import re

import numpy as np


class TextGenerator:
    model: dict

    def __init__(self):
        self.model = dict()

    def fit(self, input_dir, model_name: str = None):
        result = dict()

        for file_path in os.listdir(input_dir):
            with open(
                os.path.join(input_dir, file_path), "r", encoding="utf-8"
            ) as file:
                content = file.read()

            content = content.lower()
            content = content.strip()

            words = re.findall("[a-zа-яё]+", content)

            for index, word in enumerate(words[:-1]):
                if word in result:
                    result[word].append(words[index + 1])
                else:
                    result[word] = [words[index + 1]]

        self.model = result
        if model_name is not None:
            np.save(f"{model_name}.npy", result)

    def restore(self, model_name: str = None):
        self.model = np.load(f"{model_name}.npy", allow_pickle=True).item()

    def generate(self, length, prefix=None):
        if prefix is None:
            words = [np.random.choice(list(self.model.keys()))]
        else:
            words = prefix.split(",")

        for _ in range(length):
            last_word = words[-1]

            current_word = np.random.choice(
                self.model[last_word]
                if last_word in self.model else
                list(self.model.keys())
            )
            words.append(current_word)

        return " ".join(words)
