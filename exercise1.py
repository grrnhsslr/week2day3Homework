# Given an array of positive integers nums, return a list of, all of the negative integers.
# Ex. 1
# nums = [1, 3, 5, 7, 8]
# Expected Output: [-1, -3, -5, -7, -8]

nums_list = input("please enter a list element separated by a space ")

nums = nums_list.split()

print(nums)


def negative_list(nums):
    number_strings = [int(num) for num in nums]
    neg = [-num if num > 0 else abs(num) for num in number_strings]
    return neg


print(negative_list(nums))
