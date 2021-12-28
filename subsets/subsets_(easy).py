#subsets solution -- "bfs" -- O(2^N) time and space
#the idea is to start with the empty set and create new subsets by iteratively adding nums from arr to each exisitng subset in subsets

def find_subsets(arr):
    
    subsets = []
    
    subsets.append([])
    
    for num in arr:
        
        len_subsets = len(subsets) #len(subsets) changes, so you can't out it directly in the following for-loop
        
        for i in range(len_subsets):
            
            #saying 'new_subset = subsets[i]' does *not* create a new list, therefore you say:
    
            new_subset = list(subsets[i])
            
            #^ alternatively, say 'set = list(subsets[i])' if you cannot assume arr has only distinct (no repeating) elements
            
            new_subset.append(num)
            
            subsets.append(new_subset)
            
            print(subsets)
    
    return subsets

print(find_subsets([1,5,3]))