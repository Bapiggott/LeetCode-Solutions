class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_list = list(s)
        a = []
        #print(s_list)
        current_longest = 0
        for i in range(len(s_list)):
            if i == 0 or len(s_list) < 1:
                a += s_list[i]
            else:
                if s_list[i] not in a:
                    a += s_list[i]
                else:
                    if current_longest < len(a):
                        current_longest = len(a)
                    #current_longest = len(a)
                    index = a.index(s_list[i])
                    a = a[index + 1:] + [s_list[i]] 
            if current_longest < len(a):
                current_longest = len(a)                 
        return current_longest
