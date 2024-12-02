# Part 1 - Find Safe Sequences (min diff of three, and strictly ascending OR strictly descending)

numSafe = 0
lines = []

with open('2test.txt', 'r') as file:

    lines = file.readlines()

    for line in lines:

        nums = line.split()

        valid = True
        if len(nums) < 2:
            numSafe += 1
            continue

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

def should_remove_first(nums, candidateOneIndex, candidateTwoIndex, ascending):
    one = []
    if candidateOneIndex - 1 >= 0:
        one.append(nums[candidateOneIndex - 1])
    if candidateOneIndex + 1 < len(nums):
        one.append(nums[candidateOneIndex + 1])

    # For 'two', we remove nums[candidateTwoIndex]
    two = []
    if candidateTwoIndex - 1 >= 0:
        two.append(nums[candidateTwoIndex - 1])
    if candidateTwoIndex + 1 < len(nums):
        two.append(nums[candidateTwoIndex + 1])

    oneValid = True
    for i in range(1, len(one)):
        left = one[i - 1]
        right = one[i]

        if ascending and right < left:
            oneValid = False
        if not ascending and right > left:
            oneValid = False
        if left == right:
            oneValid = False
        if abs(left - right) > 3:
            oneValid = False

    twoValid = True
    for i in range(1, len(two)):
        left = two[i - 1]
        right = two[i]

        if ascending and right < left:
            # print("Should be ascending but isn't")
            twoValid = False
        if not ascending and right > left:
            # print("Should be descending but isn't")
            twoValid = False
        if left == right:
            # print("Both same values")
            twoValid = False
        if abs(left - right) > 3:
            # print("Too big a difference")
            twoValid = False

    if twoValid and oneValid:
        return False

    return oneValid 

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

    i = 1
    while i < len(nums):
        if not valid:
            break

        num = nums[i]
        prevNum = nums[i - 1]

        if abs(prevNum - num) > 3 or prevNum == num or (ascending and prevNum > num) or (not ascending and num > prevNum):
            if numFixes < 1:
                valid = False
                break
            if should_remove_first(nums, i - 1, i, ascending):
                nums.pop(i - 1)
                numFixes -= 1
                i = max(1, i - 1)
            else:
                nums.pop(i)
                numFixes -= 1
        else:
            i += 1

    if valid:
        numSafeWithTolerance += 1

print(numSafeWithTolerance)

