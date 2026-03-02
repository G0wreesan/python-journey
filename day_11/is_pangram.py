def is_pangram(sentence):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    sentence_set = set(sentence.lower())
    return alphabet.issubset(sentence_set)

sentence = "The quick brown fox jumps over the lazy dog"
print(is_pangram(sentence))  # Output: True