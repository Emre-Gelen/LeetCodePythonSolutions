class Solution(object):
    def twoSum(self, nums, target):
        visited = {}
        
        index = 0
        for currentValue in nums:
            remains = target - currentValue
            
            if remains in visited:
                return [visited[remains], index]
            
            visited[currentValue] = index
            
            index += 1