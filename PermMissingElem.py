"""
input array A
input length of A 
last number = A[length of A]

calculate the sum of length of A
calculate the expected sum of last number in A

lost number is factorial of last number in A divide by the factorial of length of A
output lost number
"""

A = [1, 2, 3, 5, 6]
length = len(A)
total = 0

sum_of_A = sum(A)
last_number = A[length-1]

while last_number>0:
    total += last_number
    last_number-=1

lost_number = total -sum_of_A

print("The lost number is: " + str(lost_number))