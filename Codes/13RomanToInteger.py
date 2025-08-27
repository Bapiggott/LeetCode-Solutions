class Solution:
    def romanToInt(self, s: str) -> int:
        values = {}

        values["I"] = 1
        values["V"] = 5
        values["X"] = 10
        values["L"] = 50
        values["C"] = 100
        values["D"] = 500
        values["M"] = 1000
        values["IV"] = 4
        values["IX"] = 9
        values["XL"] = 40
        values["XC"] = 90
        values["CD"] = 400
        values["CM"] = 900
        last_char = None

        value = 0
        for char in s:
            if last_char != None:
                if (last_char + char) in values:
                    #print(f"values[char: {char}, values[last_char: {values[last_char]}")
                    value += values[last_char + char]
                    last_char = None
                else:
                    #print(f"values[char: {char}, values[last_char: {last_char}]")
                    value += values[last_char]
                    last_char = char
            else:
                last_char = char
        if last_char != None:
            value += values[last_char]

        return value
