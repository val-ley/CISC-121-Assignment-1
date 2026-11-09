A = [1, 2, 3, 5, 6]
length = len(A)
total = 0

sum_of_A = sum(A)
last_number = A[length-1]

while last_number>0: #calculating the predicted sum if all numbers were in order
    total += last_number
    last_number-=1

lost_number = total -sum_of_A #predicted sum is subtracted by the actual sum of A

print("The lost number is: " + str(lost_number))