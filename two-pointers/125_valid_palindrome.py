class Solution:
    def isPalindrome(self, s: str) -> bool:
        left: int = 0
        right: int = len(s) - 1
        while left < right:
            leftascii: int = ord(s[left].lower())
            if not self.isValidAscii(leftascii):
                left += 1
                continue
            rightascii: int = ord(s[right].lower())
            if not self.isValidAscii(rightascii):
                right -= 1
                continue
            if leftascii != rightascii:
                return False
            left += 1
            right -= 1
        return True

    def isValidAscii(self, c: int) -> bool:
        return (c >= ord('a') and c <= ord('z')) or (c >= ord('0') and c <= ord('9'))
