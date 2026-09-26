class Solution(object):
    def myAtoi(self, s):
        s=s.strip()
        sign=1
        if s.startswith('-'):
            sign=-1
            s=s[1:]
        elif s.startswith('+'):
            s=s[1:]
        num=0
        for ch in s:
            if not ch.isdigit():
                break
            num=num*10+int(ch)
        num*=sign

        if num<-2**31:
            return -2**31
        if num> 2**31 -1:
            return 2**31 -1
        return num