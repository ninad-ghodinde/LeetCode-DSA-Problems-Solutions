class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=set()
        f=set()
        flag = 0
        for i in nums:
            if i in s or -i in s:
                flag=1
                f.add(i)
            if i>0:
                s.add(i)
            else:
                s.add(-i)
        if flag == 0:
            return -1
        print(s)
        print(f)
        ls = list(f)
        

print(Solution().findMaxK([-1,10,6,7,-7,1]))