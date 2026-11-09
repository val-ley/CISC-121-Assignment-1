"""
input array A
input X
create a set of all needed values using X
record time = -1

for each second in range of length A
    check if needed has A[second]
    if needed is empty
        store time taken
        break
output the time taken
        

"""

A = [1, 3, 3, 1, 2, 5, 1, 2, 3, 5, 4, 1, 2, 3, 1]
X = 5

needed = set(range(1, X + 1))
time = -1

for second in range(len(A)):
    needed.discard(A[second])
    if not needed:
        time = second
        break

print("The time it takes for the frog to cross is " + str(time) + " seconds.")