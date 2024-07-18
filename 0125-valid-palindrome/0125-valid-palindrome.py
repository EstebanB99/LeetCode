class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Remove non-alphanumeric characters and convert to lowercase
        news = ''.join(char for char in s if char.isalnum()).lower()
        
        # Initialize two pointers
        left, right = 0, len(news) - 1
        
        # Check if the string is a palindrome
        while left < right:
            if news[left] != news[right]:
                return False
            left += 1
            right -= 1
        
        return True