class Solution:
    def hammingWeight(self, n: int) -> int:
        one_bits: int = 0
        while n:
            one_bits += n & 1
            n >>= 1
        return one_bits
