def solution(nums):
    set_ = len(set(nums))
    
    if len(nums) / 2 > set_ :
        return set_
    else :
        return len(nums) / 2