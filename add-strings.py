import sys
sys.set_int_max_str_digits(10**4)

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = int(num1) + int(num2)
        return str(result)
