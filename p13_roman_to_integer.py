class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict ={'I': 1,
               'V': 5,
               'X': 10,
               'L': 50,
               'C': 100,
               'D': 500,
               'M': 1000,
               '0': 0,
              }
        
        num = 0
        i = 0
        next_char = '0'
        while( i < (len(s))):
            char = s[i]
            if i < len(s) - 1:
                next_char = s[i+1]
            num = num + dict[char]
            if i < len(s) - 1 and dict[next_char] > dict[char]:
                num = num - dict[char]
                num = num + dict[next_char] - dict[char]
                i += 2
                print(num, i)
                continue
            i+= 1
            print(num, i)
        
        return num

            
            