from json_reader import get_word_list
import math

def calculate_probability_includes(word_list, letter, location):
    words_with_letter = [word for word in word_list if letter in word and word[location] != letter]
    return len(words_with_letter) / len(word_list)

def calculate_probability_location(word_list, letter, location):
    words_with_letter = [word for word in word_list if word[location] == letter]
    return len(words_with_letter) / len(word_list)

def probability_to_bits(probability):
    return -1 * math.log2(probability)

def calculate_E(word_list, word):
    E = 0
    seen_letters = set()
    for idx, letter in enumerate(word):
        if letter not in seen_letters:
            probability = calculate_probability_includes(word_list, letter, idx)
            if probability != 0:
                E += probability * probability_to_bits(probability)
        probability = calculate_probability_location(word_list, letter, idx)
        if probability != 0:
            E += probability * probability_to_bits(probability)
        seen_letters.add(letter)
    return E 

def calculate_best_guess(word_list):
    best_word = word_list[0]
    best_E = calculate_E(word_list, best_word)
    for word in word_list:
        E = calculate_E(word_list, word)
        if E > best_E:
            best_E = E
            best_word = word
    return best_word

if __name__ == '__main__':
    word_list = get_word_list()
    best_guess = "tares"
    for i in range(5):
        print(f"Best guess: {best_guess}")
        result = input("Enter the result: ")
        if result == "y":
            break
        for idx in range(5):
            char = best_guess[idx]
            print(char)
            if result[idx] == 'g':
                word_list = [word for word in word_list if word[idx] == char]
            elif result[idx] == 'y':
                word_list = [word for word in word_list if char in word and word[idx] != char]
            elif result[idx] == '-':
                for idx_2 in range(5):
                    letter = best_guess[idx_2]
                    if letter == char and result[idx_2] == '-':
                        word_list = [word for word in word_list if word[idx_2] != char]              
            print(word_list)
        best_guess = calculate_best_guess(word_list)
  