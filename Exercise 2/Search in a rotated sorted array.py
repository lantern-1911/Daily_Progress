def search(nums,target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        
        mid = (right + left) // 2
        
        if nums[mid] == target:
            return mid
        
        elif nums[mid] >= nums[left]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            
            else:
                left = mid + 1
        
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            
            else:
                right = mid - 1
        
    return -1
nums = [4,5,6,7,0,1,2.3]
target = 0
print(search(nums,target))
