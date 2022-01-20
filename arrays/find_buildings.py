#med
#time = O(n)
#space = O(1)
def findBuildings(self, heights: List[int]) -> List[int]:
    
    curr_max = 0
    output = []
    
    for index in reversed(range(len(heights))):
        if heights[index] > curr_max:
            output.append(index)
            curr_max = heights[index]
    
    output.reverse() #O(n)
    
    return output