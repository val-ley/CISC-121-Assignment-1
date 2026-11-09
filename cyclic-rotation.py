"""
Pseudo code for cyclic rotation of an array:
A is given
K is given

while K > 0
save first value of A
then deleyte first value of A and append it into last index of A
K--

output the new A
"""

A = [3, 8, 9, 7, 6]
K = 3
new_A = A

while (K > 0):
    last = new_A.pop()       
    new_A.insert(0, last)    
    K = K - 1

print(new_A)  