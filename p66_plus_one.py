class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        number = 0
        for i in digits:
            number = number * 10 + i
        number = str(number + 1)
        lst = []
        for i in number:
            lst.append(int(i))
        return lst
        