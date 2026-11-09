"""
input x
input y
input d

value number of jumps = 0

while x> y
x+= x +d
number of jumps ++
output number of jumps

"""

X = 10
Y = 85
D = 30

jump_number = 0

while X<Y:
    X+=D
    jump_number+= 1
print("Number of jumps the frog took: " + str(jump_number))