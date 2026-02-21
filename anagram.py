class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if( len(s) != len(t)): 
            return False
        s_dict = {}
        t_dict = {}
        for i in range(len(s)):
            s_dict[s[i]] = s_dict.get(s[i], 0) + 1
            t_dict[t[i]] = t_dict.get(t[i],0) + 1
        
        return s_dict == t_dict

ALTERNATIF

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if( len(s) != len(t)): 
            return False
        
        freq_dict = {}

        for c in s:
            freq_dict[c] = freq_dict.get(c, 0) + 1

        for c in t:
            freq_dict[c] =  freq_dict.get(c, 0) - 1

        for value in freq_dict.values():
            if value != 0:
                return False

        return True        