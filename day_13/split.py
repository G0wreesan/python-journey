import sys,time

def split_sentence(sentence):
    words = sentence.split()
    return words

sentence = input("Enter a sentence: ")
words = split_sentence(sentence)
for i in range(len(words)):
    if i==0:
        print("Splitting the sentence into words...")
        time.sleep(1)
    elif i==len(words):
        print("\n All words have been displayed.")
        time.sleep(1)
    
    print(f"Word {i + 1}: {words[i]}")
    time.sleep(0.5)
