def solution(X, A):
    needed = set(range(1, X + 1)) #creates a set 1 through X

    second = 0 #stores amount of seconds passed

    for leaf in A:
        needed.discard(leaf) #if leaf is in the correct space it gets deleted from needed
        if len(needed) == 0: #needed is empty meaning the path is set for the frog to cross safely
            return second
        second += 1

    return -1 #returns -1 if path isn't clear

A = [1, 3, 3, 1, 2, 5, 1, 2, 3, 5, 4, 1, 2, 3, 1]
X = 5
print(solution(X, A)) #example solution