class Solution:
    def isHappy(self, n: int) -> bool:
        n1 = n
        ll = []
        def squarenumber(n1):
            x= 0
            for dgt in str(n1):
                x += int(dgt) ** 2
            return x
    
        while n1!=1 and n1 not in ll:
            ll.append(n1)
            n1 = squarenumber(n1)
        return n1==1
