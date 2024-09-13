class Solution(object):
    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        res=[]
        #calculating prefix XOR vals
        prefix = [0] * (len(arr) + 1)
        for i in range(len(arr)):
            prefix[i+1] = prefix[i] ^ arr[i]
        #print(prefix)
        for qry in queries:
            qry[0],qry[1]+1
            xorval=prefix[qry[0]]^prefix[qry[1]+1]
            res.append(xorval)
        return res
    
print(Solution().xorQueries([1,3,4,8],[[0,1],[1,2],[0,3],[3,3]])) #[2,7,14,8]
print(Solution().xorQueries([4,8,2,10],[[2,3],[1,3],[0,0],[0,3]])) #[8,0,4,4]