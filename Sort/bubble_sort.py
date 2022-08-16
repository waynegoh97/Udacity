# Naive approach by comparing left and right element
# If left element is bigger than right, switch
# Repeat until it is complete [(n-1) comparisons]
# Time complexity: O(n^2) since (n-1) comparisons for (n-1) iterations
# Space complexity: O(1)
def bubble_sort(bubble_list):
    size = len(bubble_list)
    for iter in range(size - 1):
        for comp in range(size - 1):
            if bubble_list[comp] > bubble_list[comp+1]:
                bubble_list[comp+1], bubble_list[comp] = bubble_list[comp], bubble_list[comp+1]
                

    return bubble_list


# Test case
bubble_list = [10,1,2,0,5]
print(bubble_sort(bubble_list))