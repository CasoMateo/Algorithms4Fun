class Solution:
    def firstUniqChar(self, s: str) -> int:

      hash_ = set()

      for i in range(len(s)): 
        if s[i] not in hash_: 
          if s[i] not in s[i + 1:]:
            return i
        hash_.add(s[i])
      return -1
