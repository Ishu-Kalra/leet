class Solution(object):
    
    def isNum(self, letter):
        if letter == '1' or letter == '2' or letter == '3' or letter == '4' or letter == '5' or letter == '6' or letter == '7' or letter == '8' or letter == '9' or letter == '0':
            print('Im here')
            return True
        else:
            return False
    
    def is_sign(self, letter):
        if letter == '+' or letter == '-':
            return True
        else:
            return False
        
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        is_negative = False
        str = str.lstrip()
        print(str)
        num = 0
        if not str:
            return num
        
        if self.is_sign(str[0]):
            if str[0] == '-':
                is_negative = True
            str = str[1:]
        
        for c in str:
            print(c)
            if self.isNum(c):
                num = num * 10 + int(c)
                print(num)
            else:
                break
            
        if is_negative:
            num = num * -1
            
        if num>2147483647:
            return 2147483647
        
        if num < -2147483648:
            return -2147483648
        
        return num
                