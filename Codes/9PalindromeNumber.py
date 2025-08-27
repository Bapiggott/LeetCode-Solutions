class Solution:
    def isPalindrome(self, x: int) -> bool:
        import math
        #x = abs(x)
        if x == 0:
            return True
        elif x < 0:
            return False
        else:
            digits = []
            length = math.floor(math.log10(abs(x))) + 1
            for i in range(math.ceil(length)):
                a = i
                i = length - i
                #print(f"i: {i}. length: {length}. x: {x}")
                digits.append(math.floor(x / (10 ** (i -1))))
                #print(f"digits[a]: {digits[a]}. x: {x}. i: {i}.")
                x = x - (digits[a] * (10 ** (i-1)))
                #print(f"x: {x}. digits: {digits}. a: {a}. i: {i}.")
            dis = math.ceil(length/2)
            #print(f"digits: {digits}. length: {length}. dis: {dis}, number: {abs(x)}")
            digits_reversed = digits.copy()
            digits_reversed.reverse()
            if digits != digits_reversed:
                print(f"digits: {digits}. reversed: {digits_reversed}")
                return False
            else:
                return True
