# find the missing number from the array 
arr = [1,2,3,5,6]

def missing_number(arr):
    n = len(arr) + 1
    expected_sum  = n * (n + 1) //2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

print(f"missing Numbers is : {missing_number(arr)}")