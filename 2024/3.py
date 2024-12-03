import re

def sum_muls(text):
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'

    matches = re.finditer(pattern, text)

    lineSum = 0

    for match in matches:
        x = int(match.group(1))
        y = int(match.group(2))
        lineSum += x * y

    return lineSum

def main():
    sum = 0
    with open('3.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            sum += sum_muls(line)

    print(sum)

if __name__ == "__main__":
    main()

