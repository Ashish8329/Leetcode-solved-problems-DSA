class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        obj = set()
        for i in nums:
            if i in obj:
                return True
            obj.add(i)  
        return False
            
        
                
        