class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==len(t):
            one="".join(sorted(s))
            two="".join(sorted(t))
            if one==two:
                return True
            else:
                return False


        else:
            return False