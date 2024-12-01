# Part 1 - Find Aggregate Difference Between Sorted Pairs

totalDifference = 0

leftValues = []
rightValues = []

with open('1.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        left, right = line.split()
        print(left)
        print(right)
        leftValues.append(left)
        rightValues.append(right)

leftValues.sort()
rightValues.sort()

for i in range(0, len(leftValues)):
    left = leftValues[i]
    right = rightValues[i]
    totalDifference += abs(int(right) - int(left))
    if i % 50 == 0:
        print("Left is: " + left)
        print("Right is: " + right)
        print("totalDifference is now: " + str(totalDifference))

print(totalDifference)

# Part 2 - 
