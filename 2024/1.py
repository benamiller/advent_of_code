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

# Part 2 - Computing Similarity Scores (aggregating left list values * frequency in right list)

similarityScore = 0

left = 0
right = 0
leftValueFreqInRight = 0
lastMatch = 0 

while left < len(leftValues) and right < len(rightValues):
    leftValue = leftValues[left]
    rightValue = rightValues[right]

    if (rightValue == leftValue):
        lastMatch = int(leftValue)
        leftValueFreqInRight += 1
        right += 1

    if (rightValue < leftValue):
        similarityScore += leftValueFreqInRight * lastMatch
        leftValueFreqInRight = 0
        right += 1

    if (rightValue > leftValue):
        similarityScore += leftValueFreqInRight * lastMatch
        leftValueFreqInRight = 0
        left += 1

print(similarityScore)
