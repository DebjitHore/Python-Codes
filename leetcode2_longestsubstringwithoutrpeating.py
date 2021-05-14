class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m=0
        if len(s)==0 :
            return 0
        if len(s)==1 or s==" ":
            return 1
        for i in range (0, len(s)-1):
            ss=s[i]
            for j in range (i+1, len(s)):
                if s[j] not in ss:
                    ss+=s[j]
                else:
                    break
            if m<len(ss):
                m=len(ss)
            
        return m