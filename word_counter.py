def word_count(text):
    words = text.split()
    return len(words)

if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    count = word_count(sentence)
    print(f"The sentence has {count} words.")
