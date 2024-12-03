import re

def sum_muls(text):
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'

    matches = re.finditer(pattern, text)

    line_sum = 0

    for match in matches:
        x = int(match.group(1))
        y = int(match.group(2))
        line_sum += x * y

    return line_sum

def main():
    sum = 0
    with open('3.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            sum += sum_muls(line)

    print(sum)

if __name__ == "__main__":
    main()


# Part 2 - Only aggregate after seeing a do() and not after seeing a don't()

def get_ops(text):
    mul_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    do_pattern = r'
