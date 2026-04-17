def count_words(text):
    \"\"\"Counts the number of words in a string.\"\"\"
    if not text:
        return 0
    return len(text.split())

if __name__ == \"__main__\":
    sample_text = input(\"Enter some text to count the words: \")
    word_count = count_words(sample_text)
    print(f\"The number of words is: {word_count}\")
