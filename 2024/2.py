# Part 1 - Find Safe Sequences (min diff of three, and strictly ascending OR strictly descending)

numSafe = 0
lines = []

with open('2test.txt', 'r') as file:

    lines = file.readlines()

    for line in lines:

        nums = line.split()

        valid = True
        ascending = int(nums[0]) < int(nums[1])

        for i in range(1, len(nums)):
            num = int(nums[i])
            prevNum = int(nums[i - 1])

            if abs(prevNum - num) > 3 or prevNum == num or (ascending and prevNum > num) or (not ascending and num > prevNum):
                valid = False 

        if valid:
            numSafe += 1

    print(numSafe)

# Part 2 - Same as part 1, but we can remove one level (value) to make the report (row) safe

numSafeWithTolerance = 0

for line in lines:
    nums = line.split()

    nums = [int(num) for num in nums]

    numFixes = 1

    ascendingVotes = 0

    for i in range(1, len(nums)):
        if nums[i - 1] < nums[i]:
            ascendingVotes += 1
        elif nums[i - 1] > nums[i]:
            ascendingVotes -= 1

    ascending = ascendingVotes > 0
    valid = True

    # If we remove a breaking value, we must compare the next value with the value before the fix for jumps > 3
    beforeFixedValue = None

    print("\nNext line\n")

    for i in range(1, len(nums)):
        num = nums[i]
        prevNum = nums[i - 1]

        if beforeFixedValue != None:
            if abs(beforeFixedValue - num) > 3:
                valid = False

        if abs(prevNum - num) > 3 or prevNum == num or (ascending and prevNum > num) or (not ascending and num > prevNum):
            if numFixes < 1:
                valid = False
            beforeFixedValue = prevNum
            numFixes -= 1

        print("\nThis loop")
        print("num: " + str(num))
        print("prevNum: " + str(prevNum))
        print("ascending: " + str(ascending))
        print("beforeFixedValue: " + str(beforeFixedValue))
        print("valid: " + str(valid))

    if valid:
        numSafeWithTolerance += 1

print(numSafeWithTolerance)

