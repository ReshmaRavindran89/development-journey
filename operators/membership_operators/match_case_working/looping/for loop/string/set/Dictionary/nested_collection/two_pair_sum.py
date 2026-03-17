
# Two pair sum :-
nums =[2,3,4,5]

def two_sum_sorted(nums, target):
    left = 0
    right = len(nums) - 1
    curr_sum = 0
    while left < right:
        curr_sum = nums[left] + nums[right]
        
        if curr_sum == target:
            return [left, right]
        
        elif curr_sum < target:
            left += 1  # Need a larger sum
        else:
            right -= 1 # Need a smaller sum
    return[]

