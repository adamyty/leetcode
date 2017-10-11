from collections import defaultdict
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        rlen = 0
        # declare an empty dictionary to store s. dict key : s[i], dict value : i
        dictMap = defaultdict(list)
        """
        slicing window consist of lindex and rindex

               lidx  ridx
               |     |
        s : a  b  c  a  b  c  b  b
        
        sudo code :
        for each e in s:
            if e in dict:
                1. update lidx if e locate in slicing window
                2. update dict[e] = e.idx
                3. update rlen if necessary
            else:
                1. add dict[e] = e.idx
                2. update rlen if necessary
        """
        lindex = 0
        rindex = 0
        
        for rindex, value in enumerate(s):
            if value in dictMap:
                lindex = max(lindex, dictMap[value] + 1)
                del dictMap[value]
                dictMap[value] = rindex
                rlen = max(rlen, rindex - lindex + 1)
            else:
                dictMap[value] = rindex
                rlen = max(rlen, rindex - lindex +1)

        return rlen

            
solution = Solution()
s = "abcabcbb"
print('s : ', s)
dictMap = defaultdict(list)
for index, value in enumerate(s):
    dictMap[value].append(index)
for value in dictMap:
    print(' value : %r index : %r'%(value, dictMap[value]))

rlen = solution.lengthOfLongestSubstring(s)
print('length Of Longest Substring : ', rlen)
