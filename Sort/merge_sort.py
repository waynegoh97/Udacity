# Divide and conquer approach
# Break up all the arrays into 1 element each
# Attempt to pair each element up and do comparison
# Repeat the pairing until it forms back to one entire array
# Time complexity: n possible comparisons, logn iterations
# O(nlogn)
# Space complexity: O(n)

def merge(merge_list):
    size = len(merge_list)
    for i in range(size):
        


# Test case

merge_list = [8,3,1,7,0,10,2]
print(merge(merge_list))