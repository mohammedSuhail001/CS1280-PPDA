# Modify the word count program to also count the frequency of each word in the sentence.
def word_count(sentence):
    words = sentence.split()
    word_freq = {word: words.count(word) for word in set(words)}
    return len(words), word_freq

sentence = input("Enter a sentence: ")
count, frequency = word_count(sentence)
print(f"Total words: {count}\nWord Frequency: {frequency}")
