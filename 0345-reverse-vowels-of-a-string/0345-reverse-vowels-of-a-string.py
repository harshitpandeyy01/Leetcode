class Solution(object):
    def reverseVowels(self, s):
        
        vowels = set('aeiouAEIOU')  # Set of vowels (both lower and upper case)
        s = list(s)  # Convert string to a list for easier swapping
        left, right = 0, len(s) - 1

        while left < right:
            # Move left pointer to the next vowel
            while left < right and s[left] not in vowels:
                left += 1
            # Move right pointer to the previous vowel
            while left < right and s[right] not in vowels:
                right -= 1
            
            # Swap the vowels at the left and right pointers
            if left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        
        return ''.join(s)  # Convert the list back to a string
