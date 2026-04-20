# A simple word counter script

def count_words(text):
    """Counts the number of words in a given string."""
    words = text.split()
    return len(words)

if __name__ == "__main__":
    sample_text = "This is a sample sentence for word counting."
    word_count = count_words(sample_text)
    print(f"The text has {word_count} words.")
