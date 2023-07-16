class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        Merges the characters from word1 and word2 alternatively.
        Returns the merged string.

        :param word1: The first string.
        :type word1: str
        :param word2: The second string.
        :type word2: str
        :return: The merged string.
        :rtype: str
        """
        merged = ""
        len1, len2 = len(word1), len(word2)
        max_len = max(len1, len2)

        for i in range(max_len):
            if i < len1:
                merged += word1[i]
            if i < len2:
                merged += word2[i]

        return merged
# Create an instance of the Solution class
solution = Solution()

# Call the mergeAlternately method with word1 and word2
word1 = "Hello"
word2 = "omosh"
result = solution.mergeAlternately(word1, word2)

# Print the result
print(result)


        
    