from typing import List

list1 = [0,1,0,3,12]

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        move_times = 0
        for i in range(len(nums)):
            if nums[i + move_times] == 0:
                nums.append(nums.pop((i + move_times)))
                move_times -= 1
        return nums

    def moveZeroes2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos =0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                if pos!= i:
                    nums[i],nums[pos] = nums[pos],nums[i]
            
                pos +=1
            print(nums)
        return nums
sol = Solution()
print(sol.moveZeroes2(list1))