class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Convert string to list for easy character swaps
        s = list(s)
        p, q = 0, len(s) - 1  # Initialize two pointers

        # Loop until the two pointers cross each other
        while p < q:
            # Move p to the right if it's not pointing to a letter
            if not s[p].isalpha():
                p += 1
            # Move q to the left if it's not pointing to a letter
            elif not s[q].isalpha():
                q -= 1
            # If both p and q point to letters, swap them and move both pointers inward
            else:
                s[p], s[q] = s[q], s[p]
                p += 1
                q -= 1

        # Join the list back into a string and return it
        return ''.join(s)
