class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result = []
        
        for num in nums:
            digits = str(num)
            
            for d in digits:
                result.append(int(d))
        
        return result