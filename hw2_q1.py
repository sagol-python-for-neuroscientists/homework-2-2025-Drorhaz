MORSE_CODE = {'A': '.-', 'B': '-...', 'C': '-.-.',
              'D': '-..', 'E': '.', 'F': '..-.',
              'G': '--.', 'H': '....', 'I': '..',
              'J': '.---', 'K': '-.-', 'L': '.-..',
              'M': '--', 'N': '-.', 'O': '---',
              'P': '.--.', 'Q': '--.-', 'R': '.-.',
              'S': '...', 'T': '-', 'U': '..-',
              'V': '...-', 'W': '.--', 'X': '-..-',
              'Y': '-.--', 'Z': '--..',
              '0': '-----', '1': '.----', '2': '..---',
              '3': '...--', '4': '....-', '5': '.....',
              '6': '-....', '7': '--...', '8': '---..',
              '9': '----.',
              '.': '.-.-.-', ',': '--..--', ':': '---...',
              "'": '.----.', '-': '-....-'}


def english_to_morse(input_file="lorem.txt", output_file="lorem_morse.txt"):
    with open(input_file, "r") as f:
        text = f.read().upper()

    # Flatten entire text into words
    words = text.split()

    # Convert each word character-by-character using get (preserve structure!)
    morse_lines = []
    for word in words:
        morse_word = ''.join(MORSE_CODE.get(c, '') for c in word)
        morse_lines.append(morse_word)

    # Write each Morse word in a new line, with a trailing newline at the end
    with open(output_file, "w") as f:
        f.write('\n'.join(morse_lines) + '\n')


if __name__ == "__main__":
    english_to_morse()
    print("Done.")
