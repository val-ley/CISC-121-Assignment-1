X = 10 #frog position
Y = 85 #target position
D = 30 #jump increment

jump_number = 0 # number of jumps the frog has taken

while X<Y: #while frog position is smaller than target position
    X+=D # increase frog position by jump increment
    jump_number+= 1 #count number of jumps the frog took
print("Number of jumps the frog took: " + str(jump_number))