class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans = ''
        #print(strs)
        strs = sorted(strs, key = len)
        #print(strs)
        if strs:
            check = strs[0]
            strs = strs[1:]
            if strs:
                #print('Imma here')
                letter_specific_flag = True
                j = 0
                i = 0
                while i < len(check):
                    while j < len(strs):
                        #print(strs[j], strs[j][i], check, check[i])
                        if strs[j][i] != check[i]:
                            letter_specific_flag = False
                            break
                        j +=1
                    
                    if letter_specific_flag:
                        ans += check[i]
                    else:
                        return ans
                    i += 1
                    j = 0
                    letter_specific_flag = True  
            else:
                return check
        
        return ans
        