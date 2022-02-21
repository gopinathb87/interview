class Solution:
    def lengthOfLongestSubstring(self, s):
        longest = 0
        l = 0
        lib = {}
        
        for r,c in enumerate(s):
            if c in lib:
                l = max(l, lib[c]+1)
            lib[c] = r
            print(l,r)
            longest= max(r- l + 1, longest)
        print(lib)
        return longest
        
s = "abcabcdbb"
zs= "bbcbabca"
l ="01122445"

"abc"

sol = Solution()
print(sol.lengthOfLongestSubstring(s))
