class Solution:
    def reverse(self, x: int)-> int:
            if x > 0:
                #x = list(map(int, str(x)))
                #print("Reversed digits:", list(reversed(x)))
                rev = int(str(x)[::-1])#return int(map(list, int(reversed(x))))
                return 0 if rev > 2**31 - 1 else rev
            else:
                x = x*-1

                rev= int(str(x)[::-1])
                return 0 if rev > 2**31 - 1 else -rev
