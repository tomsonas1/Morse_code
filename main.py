#morse alphabet
ALPHABET_TO_MORSE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                  'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                  'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                  'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
                  '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ',': '--..--', '.': '.-.-.-',
                  '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': ' '}


MORSE_TO_ALPHABET = {v:k for k, v in ALPHABET_TO_MORSE.items()}
def main():
    enc_or_dec = input(' Enter "E" to encode, "D" to decode \n').upper()
    if enc_or_dec == "E":
        error_text = "Use only ASCII symbols"
        message = get_message(ALPHABET_TO_MORSE, error_text)
        print(encode_to_morse(message))
    elif enc_or_dec == "D":
        error_text = "Enter Morse code"
        message = get_message(MORSE_TO_ALPHABET, error_text)
        print(decode_from_morse(message))
    else:
        main()






def get_message(alphabet, error_text):
    msg = input('Write message:\n').upper()
    for i in msg:
        if i not in alphabet.keys():
            print(error_text)
            return get_message(alphabet, error_text)

    return msg


def encode_to_morse(message):
    encoded_message = ''
    """If it is symbol, replace it with morse symbols and add one space
    After each word add 3 spaces
    """
    for i in message:
        if i != ' ':
            encoded_message += ALPHABET_TO_MORSE[i] + ' '
        else:
            encoded_message += ' ' * 2
    return encoded_message


def decode_from_morse(morse_message):
    morse_words = morse_message.split('   ')
    decoded_message = []
    decoded_word = ''
    for word in morse_words:
        morse_char = word.split(' ')

        for char in morse_char:
            for key, value in MORSE_TO_ALPHABET.items():
                if key == char:
                    decoded_word += value

        decoded_message.append(decoded_word)
        decoded_word = ''

    return ' '.join(decoded_message)


if __name__ == '__main__':
    main()
