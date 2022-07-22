class MorseCodeLogic:
    def __init__(self):
        self.conversion_table = {
            " ": "/",
            "a": ".-",
            "b": "-...",
            "c": "-.-.",
            "d": "-..",
            "e": ".",
            "f": "..-.",
            "g": "--.",
            "h": "....",
            "i": "..",
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
            "10": "-----",
            ".": ".-.-.-",
            ",": "--..--",
            "?": "..--..",
            "'": ".----.",
            "!": "-.-.--",
            "(": "-.--.",
            ")": "-.--.-",
            "&": ".-...",
            ":": "---...",
            ";": "-.-.-.",
            "=": "-...-"
        }
        self.un_conversion_table = dict([(value, key) for key, value in self.conversion_table.items()])
    def to_morse(self, str: str) -> str:
        """This method accepts a string of words, spaces and characters and compares it to the internal
        conversion table. It returns a string representation of the morse code"""
        characters = list(str)
        output = []
        #-- Loop through characters and convert to morse representation --#
        for x in characters:
            x = x.lower()
            if x in self.conversion_table:
                output.append(self.conversion_table[x])
        return " ".join(output)


    def from_morse(self, str:str) -> str:
        characters = [" ".join(x.split(" ")) for x in str.split('/')]
        output= ''
        for x in characters:
            word = x.strip().split(" ")
            for y in word:
                if y in self.un_conversion_table:
                    output += self.un_conversion_table[y]
            output += " "
        return output
