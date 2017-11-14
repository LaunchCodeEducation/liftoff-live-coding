'''
You are given two arrays of identical size.

You need to zip the arrays together maintaing their order

example
arr1 = [1,5,2]
arr2 = [3,6,4]
answer = [1,3,5,6,2,4]
'''


def zip_arrs(arr1, arr2):
    new_arr = []
    for i in range(0, len(arr1)):
        new_arr.append(arr1[i])
        new_arr.append(arr2[i])

    return new_arr

print(zip_arrs([1,5,2], [3,6,4]))