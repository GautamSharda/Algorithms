#one-pass solution, O(n) time, O(n) space for ranges/returning array
def composeRanges(nums):
    
    if len(nums) == 0:
        return []
    
    initial = nums[0]
    ranges = []
    curr = 0
    
    while curr < len(nums):
        
        if curr == len(nums)-1:
            end = nums[curr]
            if initial == end:
                ranges.append(f"{initial}")
            else:
                ranges.append(f"{initial}->{end}")
            return ranges
            curr += 1
                
        if nums[curr+1] != nums[curr]+1:
            end = nums[curr]
            if initial == end:
                ranges.append(f"{initial}")
            else:
                ranges.append(f"{initial}->{end}")
            initial = nums[curr+1]
            curr += 1
        else:
            curr += 1
