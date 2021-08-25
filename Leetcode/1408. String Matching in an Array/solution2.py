class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        concat = ' '.join(words)
        substrings = [word for word in words if concat.count(word) >= 2]
        
        return substrings
