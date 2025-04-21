MORSE_CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
              'D': '-..',    'E': '.',      'F': '..-.',
              'G': '--.',    'H': '....',   'I': '..',
              'J': '.---',   'K': '-.-',    'L': '.-..',
              'M': '--',     'N': '-.',     'O': '---',
              'P': '.--.',   'Q': '--.-',   'R': '.-.',
              'S': '...',    'T': '-',      'U': '..-',
              'V': '...-',   'W': '.--',    'X': '-..-',
              'Y': '-.--',   'Z': '--..',

              '0': '-----',  '1': '.----',  '2': '..---',
              '3': '...--',  '4': '....-',  '5': '.....',
              '6': '-....',  '7': '--...',  '8': '---..',
              '9': '----.',

              '.': '.-.-.-', ',': '--..--', ':': '---...',
              "'": '.----.', '-': '-....-',
              }


def english_to_morse(
    input_file: str = "lorem.txt",
    output_file: str = "lorem_morse.txt"
):
    
    

    with open(input_file, "r") as f:
        text = f.read()
        text = text.upper()
        words = text.split()

    morse_words = [ ''.join(MORSE_CODE[letter] for letter in word if letter in MORSE_CODE)
                        for word in words
    ]

    morse_text = '\n'.join(morse_words)

    with open(output_file, "w") as f:
        f.write(morse_text)


if __name__ == "__main__":
    english_to_morse()
    print("english to morse completed")
