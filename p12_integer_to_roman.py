class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        str = ''
        thousands = num // 1000
        num = num - thousands * 1000
        str = str + 'M' * thousands
        if (num >=900):
            str = str + 'CM'
            num = num - 900
        five_hundreds = num // 500
        num = num - 500 * five_hundreds
        str += 'D' * five_hundreds
        if (num >= 400):
            str += 'CD'
            num = num - 400
        hundreds = num // 100
        num = num - 100 * hundreds
        str += 'C' * hundreds
        if (num >= 90):
            num = num - 90
            str += 'XC'
        fiftees = num // 50
        num = num - 50 * fiftees
        str += 'L' * fiftees
        if num >= 40:
            num = num - 40
            str += 'XL'
        tens = num // 10
        num = num - tens * 10
        str += 'X' * tens
        if num == 9:
            str += 'IX'
            num = num - 9
        fives = num // 5
        num = num - 5 * fives
        str += 'V' * fives
        if num == 4:
            num = num - 4
            str += 'IV'
        ones = num // 1
        num = num - 1 * ones
        str += ones * 'I'
        if num ==0:
            return str
        else:
            return 'Logic error'