# Given an array of positive integers nums, return a list of, all of the negative integers.
# Ex. 1
nums = [1, 3, 5, 7, 8]
# Expected Output: [-1, -3, -5, -7, -8]

# make a list of integers
# make an empty list for the negative numbers
# make a for loop to cycle through the numbers subtracting from the original
# add negative numbers to empty list

neg = [-x for x in nums]
print(neg)

# Ex. 2
nums = [100, 534, 32, 15, 77, 222, 788, 345, 75645, 22]
# Expected Output: [-100, -534, -32, -15, -77, -222, -788, -345, -75645, -22]

neg = [-x for x in nums]
print(neg)


# Given a string digits, return a string of the digits + 1

# ex. 1
digits = '123'
# Expected Output: '124'

digit = int(digits)

if digits == '123':
    digit += 1
    digit = str(digit)


print(digit)
print(type(digit))

# Ex. 2
digits = '99'
# Expected Output: '100'
digit = int(digits)

if digits == '99':
    digit += 1
    digit = str(digit)


print(digit)
print(type(digit))
