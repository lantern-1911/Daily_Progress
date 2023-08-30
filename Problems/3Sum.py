def threeSum(nums):
        nums.sort()
        result = set()
    
        for i in range(0,len(nums)-2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum == 0:
                    result.add((nums[i] , nums[left] , nums[right]))
                if current_sum > 0: 
                    right -= 1
                elif current_sum < 0:
                    left += 1
                else:
                    left += 1
                    right -= 1
        return result
nums = [7,3,2,1,5]
print(threeSum(nums))