# 9 - Given an integer x, return true if x is a palindrome and false otherwise.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        string_x = str(x)
        reverse = "".join(reversed(string_x))

        if string_x == reverse:
            return True

        else:
            return False
