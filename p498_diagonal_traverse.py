class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        print(matrix)
        i = 0
        j = 0
        lst = []
        counter = 0
        if not matrix or not matrix[0]:
            return lst
        length = len(matrix) * len(matrix[0])
        flag = True
        while counter < length:
            counter = counter + 1
            lst.append(matrix[i][j])
            if flag:
                i = i - 1
                j = j + 1
            else:
                i = i + 1
                j = j - 1
            if i < 0 or j >= len(matrix[0]):
                flag = False
                if i<0 and j>=len(matrix[0]):
                    i = i +2
                    j = j-1
                elif i < 0:
                    i = i +1
                else:
                    i = i + 2
                    j = j -1
            if i >= len(matrix) or j < 0:
                flag = True
                if i >= len(matrix) and j < 0:
                    j = j + 2
                    i = i -1
                elif j < 0:
                    j = j + 1
                else:
                    j = j + 2
                    i = i - 1
        return lst