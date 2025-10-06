class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        sign =1 
        num =0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        while i < n and s[i] ==' ':
            i+=1
        if i == n:
            return 0
        if s[i] =='-':
            sign =-1
            i+=1
        elif s[i]=='+':
            i+=1
        
        while i < n and s[i].isdigit():
            digit = int(s[i])
            if num > (INT_MAX - digit) // 10:
                if sign ==1:
                    return INT_MAX
                else:
                    return INT_MIN
            num = num * 10 +digit
            i+=1
        num = num*sign
        if num < INT_MIN:
            return INT_MIN
        elif num > INT_MAX:
            return INT_MAX
        else:
            return num
