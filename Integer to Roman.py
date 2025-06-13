class Roman:
    def __init__(self):
        self.roman_map = {
            1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X',
            40: 'XL', 50: 'L', 90: 'XC', 100: 'C',
            400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'
        }
        self.value_symbol_pairs =  [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
    def to_roman(self, integer_value):
        roman_numeral = []
        for value, symbol in self.value_symbol_pairs:
            while integer_value >= value:
                roman_numeral.append(symbol)
                integer_value -= value
            if integer_value == 0:
                break
        return "".join(roman_numeral)
if __name__ == "__main__":
    converter = Roman()
    while True:
        user_number_str = input("Enter an integer (1-3999) to convert to Roman numerals(or q to quit) :")
        if user_number_str.lower() == 'q':
            print("Exiting program.")
            break
        user_number = int(user_number_str)
        roman_value = converter.to_roman(user_number)
        print("The Roman numeral for", user_number,"is :", roman_value)
        print("-" * 30)