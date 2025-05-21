def trailing_zeroes(n):
    count = 0
    while n >= 5:
        n = n // 5        # divide n by 5
        count += n        # add that result to count
    return count
print(trailing_zeroes(int(input())))