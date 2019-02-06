class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        arr = [[0 for _ in range(700)] for _ in range(numRows)]

        row = 0
        col = 0
        flag = True
        if numRows == 1:
            return s
        for char in s:
            #print(row, col, char)
            arr[row][col] = char
            if row == numRows -1:
                flag = False
                
            if flag == False:
                row = row - 1
                col = col + 1
            else:
                row = row + 1
                
            if row == 0:
                flag = True
            
            
        s2 = ''
        for i in arr:
            for j in i:
                if j != 0:
                    s2 = s2 + j
        return(s2)
                