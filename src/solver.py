# src/solver.py

import os
from collections import Counter


class WordleSolver:
    def __init__(self):
        self.word_list = self.load_word_list()
        self.possible_words = self.word_list.copy()

    def load_word_list(self):
        file_path = os.path.join(
            os.path.dirname(__file__), "..", "data", "word_list.txt"
        )
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Word list file '{file_path}' not found.")
        with open(file_path, "r") as file:
            words = [word.strip().lower() for word in file if len(word.strip()) == 5]
        return words

    def reset(self):
        self.possible_words = self.word_list.copy()

    def update_possible_words(self, guess, feedback):
        new_possible_words = []
        for word in self.possible_words:
            match = True
            for i in range(5):
                if feedback[i] == "g":
                    if word[i] != guess[i]:
                        match = False
                        break
                elif feedback[i] == "y":
                    if guess[i] not in word or word[i] == guess[i]:
                        match = False
                        break
                elif feedback[i] == "_":
                    # Handle multiple occurrences of letters
                    if guess[i] in word:
                        match = False
                        break
            if match:
                new_possible_words.append(word)
        self.possible_words = new_possible_words

    def get_letter_frequencies(self):
        letter_counts = Counter()
        for word in self.possible_words:
            letter_counts.update(
                set(word)
            )  # Use set to avoid counting duplicate letters
        return letter_counts

    def suggest_next_guess(self):
        letter_freq = self.get_letter_frequencies()
        scored_words = []
        for word in self.possible_words:
            score = sum(letter_freq[letter] for letter in set(word))
            scored_words.append((score, word))
        scored_words.sort(reverse=True)
        return [word for score, word in scored_words]
