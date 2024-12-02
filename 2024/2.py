numSafe = 0

with open('2.txt', 'r') as file:

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






