# Qeustion:- find the second largest number form the given array

arr = [10,20,30,20]

def second_largest(arr):
    first = second = -1
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num < first and num > second:
            second = num
    return second

print(f"Second largest number is: {second_largest(arr)}")