A = [3, 8, 3, 9, 9]

while len(A) > 1: #continue pairing numbers untill 1 is left
    first = A[0]
    pair_index = None
    for number in range(1, len(A)): 
        if A[number] == first: #always checking with the first number 
            pair_index = number #pair is found and the index gets stored
    if pair_index == None: #if no pair is found
        break

    A.pop(pair_index) #pairs get deleted
    A.pop(0)

unpaired_number = A[0]
print("The unpaired number is: " + str(unpaired_number))