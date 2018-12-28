class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if abs(x)==0:
            return 0;
        res='';
        neg = False;
        if x <0:
            x = -x;
            neg= True;
        while x >0:
            res +=str(x%10);
            x =x//10;
        
        res =int(res);
        if neg:
            res =-res;
        
        if -(2**31) >res or (2**31) -1 <res:
            return 0;
        return res;