class Solution:
    def reverseBits(self, n: int) -> int:
        val = 0
        for idx in range(32):
         
    
            pop = int(n % 2)
            push = val*2 + pop 
            val = push
            n = (n/2)
        return push
