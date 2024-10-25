class Solution(object):
    def isPalindrome(self, s):
         # Normalize the string by converting to lowercase and removing non-alphanumeric characters
        normalized_str = ''.join(char.lower() for char in s if char.isalnum())
        
        # Check if the normalized string is a palindrome
        return normalized_str == normalized_str[::-1]

# Example usage:
solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))  
print(solution.isPalindrome("race a car"))                      
print(solution.isPalindrome(" "))                               