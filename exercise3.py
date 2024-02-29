# Given a string digits, return a string of the digits + 1

# ex. 1
# digits = '123'
# Expected Output: '124'


count = input('enter a number ')

def plus1(count):
    if isinstance(count, str):
        count = int(count)
        count += 1
    return count


print(plus1(count))
