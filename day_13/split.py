import sys

def split_sentence(sentence):
    words = sentence.split()
    return words

sentence = input("Enter a sentence: ")
words = split_sentence(sentence)
for i in range(len(words)):
    print(f"Word {i + 1}: {words[i]}")