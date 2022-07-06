morse_code = {
                 "a": ".-",
                 "b": "-...",
                 "c": "-.-.",
                 "d": "-..",
                 "e": ".",
                 "f": "..-.",
                 "g": "--.",
                 "h": "....",
                 "i":"..",
                 "j": ".---",
                 "k": "-.-",
                 "l": ".-..",
                 "m": "--",
                 "n": "-.",
                "o": "---",
                "p": ".--.",
                "q": "--.-",
                "r": ".-.",
                "s": "...",
                "t": "-",
                "u": "..-",
                "v": "...-",
                "w": ".--",
                "x": "-..-",
                "y": "-.--",
                "z": "--..",
                "1": ".----",
                "2": "..---",
                "3": "...--",
                "4": "....-",
                "5": ".....",
                "6": "-....",
                "7": "--...",
                "8": "---..",
                "9": "----.",
                "0": "-----",
                " ": "I'm a space",

}


word= input("Enter a word to convert it in morse code -> ").lower()
converted = []
for letter in word:
    converted.append(morse_code[letter])
print(f"{word} : {converted}")