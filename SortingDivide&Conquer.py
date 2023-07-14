# Merge Sort, Quicksort and Divide-n-Conquer Algorithms in Python


def bubble_sort(nums):

    for _ in range(len(nums)-1):
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
    return  nums

# timecomlexity is o(n)2 and spacecomlexity is o(1)
# print(bubble_sort([4, 2, 6, 3, 4, 6, 2, 1]))

nums=[4, 2, 6, 3, 4, 6, 2, 1]



