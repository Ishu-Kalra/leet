class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '': return 0
        window = s[0]
        p = 0
        k = 1
        size = 1
        max_size = 1
        while True:
            p += 1
            ##print(window, s[p], p, len(s), size)
            if max_size < size: max_size = size
            if p == len(s): break
            
            if s[p] not in window:
                window += s[p]
                size += 1
            else:
                size = 1
                p = k
                window = s[k]
                k+=1
        return max_size
            