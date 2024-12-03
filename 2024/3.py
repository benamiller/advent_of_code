import re

# Part 1 - Aggregate all mul(Xi,Yi)s

def sum_muls(text):
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'

    matches = re.finditer(pattern, text)

    line_sum = 0

    for match in matches:
        x = int(match.group(1))
        y = int(match.group(2))
        line_sum += x * y

    return line_sum

# Part 2 - Only aggregate after seeing a do() and not after seeing a don't()

def get_do_dont_sum(text):
    mul_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    do_pattern = r'do\(\)'
    dont_pattern = r'don\'t\(\)'

    ops = []

    for match in re.finditer(mul_pattern, text):
        ops.append({
            'type': 'mul',
            'pos': match.start(),
            'x': int(match.group(1)),
            'y': int(match.group(2))
        })

    for match in re.finditer(do_pattern, text):
        ops.append({
            'type': 'do',
            'pos': match.start()
        })

    for match in re.finditer(dont_pattern, text):
        ops.append({
            'type': 'dont',
            'pos': match.start()
        })

    ops.sort(key=lambda x: x['pos'])

    line_sum = 0
    should_sum = True

    print(ops)
    for op in ops:
        if op['type'] == 'mul':
            if should_sum:
                line_sum += op['x'] * op['y']
            else:
        elif op['type'] == 'do':
            should_sum = True
        elif op['type'] == 'dont':
            should_sum = False

    return line_sum
    
def main():
    lines = []
    big_string = ""

    sum = 0
    with open('3.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            sum += sum_muls(line)
            big_string += line

    print(sum)

    do_dont_sum = get_do_dont_sum(big_string)

    print(do_dont_sum)

if __name__ == "__main__":
    main()



