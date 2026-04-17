
def text_to_morse(text):
    MORSE_CODE_DICT = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
        '9': '----.', '0': '-----', ' ': '/'
    }
    text = text.upper()
    encoded_message = []
    for char in text:
        if char in MORSE_CODE_DICT:
            encoded_message.append(MORSE_CODE_DICT[char])
    return ' '.join(encoded_message)

def morse_to_text(morse):
    MORSE_CODE_DICT = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
        '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
        '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
        '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
        '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2', '...--': '3',
        '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8',
        '----.': '9', '-----': '0', '/': ' '
    }
    decoded_message = []
    words = morse.split(' / ')
    for word in words:
        chars = word.split(' ')
        for char in chars:
            if char in MORSE_CODE_DICT:
                decoded_message.append(MORSE_CODE_DICT[char])
    return ''.join(decoded_message)

if __name__ == "__main__":
    message = "Hello World"
    encoded = text_to_morse(message)
    print(f"Text: {message}")
    print(f"Morse: {encoded}")
    
    decoded = morse_to_text(encoded)
    print(f"Decoded: {decoded}")
