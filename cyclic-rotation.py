A = [3, 8, 9, 7, 6]
K = 3
new_A = A

while (K > 0): #loop K times
    last = new_A.pop() #save last number in A  
    new_A.insert(0, last) #insert last number at the end of A
    K = K - 1

print(new_A) #output the updated A array