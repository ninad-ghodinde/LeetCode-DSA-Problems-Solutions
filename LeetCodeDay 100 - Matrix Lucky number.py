class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        columns= [] 
        for i in range(len(matrix[0])):
            columns.append([matrix[j][i] for j in range(len(matrix))])
        #print(columns)
        for matrixx in matrix:
            place = matrixx.index(min(matrixx))
            #print(place)
            if min(matrixx) == max(columns[place]):
                return [min(matrixx)]
        
        

print(Solution().luckyNumbers([[7,6,8],[9,11,13],[15,16,17]])) # [15]
print(Solution().luckyNumbers([[7,8],[1,2]])) # [7]
print(Solution().luckyNumbers([[1,10,4,2],[9,3,8,7],[15,16,17,12]])) # [12]