def is_pangram(sentence):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    sentence_set = set(sentence.lower())
    return alphabet.issubset(sentence_set)


test_sentence = "The quick brown fox jumps over the lazy dog"
print(is_pangram(test_sentence)) 


input_sentence = input("Enter a sentence: ")
if is_pangram(input_sentence):
    print("The sentence is a pangram.")
else:
    print("The sentence is not a pangram.")