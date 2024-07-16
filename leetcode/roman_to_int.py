class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0

        for char in s:
            print(char)
            if char == "I":
                total += 1

            if char == "L":
                total += 50

            if char == "V":
                total += 5

            if char == "M":
                total += 1000

            if char == "IV":
                total += 4

            if char == "XC":
                total += 90

            if char == "CM":
                total += 900

        return total
