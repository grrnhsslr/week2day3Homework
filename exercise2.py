# Given a string, return a list of all of the digits in the string.
# Ex. 1
# address = "123 Real Street, Apt. 2, Springfield, OR 43498"
# Expected Output: ['1', '2', '3', '2', '4', '3', '4', '9', '8']

address = input("please enter your address ")

def addy_nums(address):
    newList = [int(i) for i in address[:] if i.isdigit()]
    return newList

print(addy_nums(address))
