'''
Given an array of integers, you need to:
find the largest value
find the smallest value
subtract the largest value from the smallest value
return the difference
'''

def min_max_diff(sample_arr):
    highest = sample_arr[0]
    lowest = sample_arr[0]
    for value in sample_arr:
        if value >= highest:
            highest = value
        elif value <= lowest:
            lowest = value
    
    diff = highest - lowest
    return diff


print(min_max_diff([6,15,2,3,1,4,5,6,7,21]))
pritn(min_max_diff([1,23,4,5,6,7,8,9]))