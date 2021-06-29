from typing import List


def calSumOfNums(nums:List[int], target:int)->List[int]:
    return [indx for indx,num in enumerate(nums) if target-num in nums if target-num == num  and nums.count(num)>1 or target-num!=num]  
    
    

a = [3,3,4,5,5]
print(calSumOfNums(a,6))