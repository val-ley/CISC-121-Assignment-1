"""
input array A

for number in array 
    store first number in array then compare to every single other number
    if pair found then delete first number and paired number from the list
    if not then exit for loop and declare that number the unpaired number
"""

A = [3, 8, 3, 9, 9]

while len(A) > 1:
    first = A[0]
    pair_index = None
    for number in range(1, len(A)):
        if A[number] == first: 
            pair_index = number
    if pair_index == None:
        break

    A.pop(pair_index)
    A.pop(0)

unpaired_number = A[0]
print("The unpaired number is: " + str(unpaired_number))