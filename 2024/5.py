def parse_rules(rule_lines):
    rules = []
    for line in rule_lines:
        line = line.strip()
        if not line:
            continue
        left, right = line.split('|')
        rules.append((int(left), int(right)))
    return rules

def parse_updates(update_lines):
    updates = []
    for line in update_lines:
        line = line.strip()
        if not line:
            continue
        pages = [int(x) for x in line.split(',')]
        updates.append(pages)
    return updates

def is_correctly_ordered(update, rules):
    page_positions = {page: i for i, page in enumerate(update)}
    
    for (X, Y) in rules:
        # Only check if both X and Y are in this update
        if X in page_positions and Y in page_positions:
            if page_positions[X] >= page_positions[Y]:
                return False
    return True

def solve():
    rule_lines = []
    update_lines = []

    with open('5test.txt', 'r') as file:
        lines = file.readlines()
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if line == "":
                break
            rule_lines.append(line)
            i += 1
        while i < len(lines):
            line = lines[i].strip()
            update_lines.append(line)
            i += 1

    print("Rule lines")
    print(rule_lines)
    print("Update lines")
    print(update_lines)

        
    rules = parse_rules(rule_lines)
    updates = parse_updates(update_lines)
    
    sum_of_middles = 0
    for update in updates:
        if is_correctly_ordered(update, rules):
            # Find the middle page - Nearly missed the whole point
            middle_index = len(update) // 2
            middle_page = update[middle_index]
            sum_of_middles += middle_page
    
    print(sum_of_middles)

if __name__ == "__main__":
    solve()

