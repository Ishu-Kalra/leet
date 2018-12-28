'''
Make sure that the inputted integer and the reverse of it do not ovwerflow. Checking only the inputted integer i.e. x is the wrong approach and I spent close to 30 minutes figuring this out.
'''
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y = 2 ** 31
        k = 0
        if x > 0:
            k = int(str(x)[::-1])
            if x > y - 1 or k > y - 1:
                return 0
            else:
                return k
        else:
            x = x * -1
            k = int(str(x)[::-1]) * -1
            if -x < -y or k < -y:
                return 0
            else:
                return k
