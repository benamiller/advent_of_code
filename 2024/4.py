def find_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    
    directions = [
        (0, 1), (1, 1), (1, 0), (1, -1),
        (0, -1), (-1, -1), (-1, 0), (-1, 1)
    ]
    
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols
    
    def check_direction(x, y, dx, dy):
        word = "XMAS"
        for i, char in enumerate(word):
            new_x, new_y = x + i * dx, y + i * dy
            if not is_valid(new_x, new_y) or grid[new_x][new_y] != char:
                return False
        return True
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'X':
                for dx, dy in directions:
                    if check_direction(i, j, dx, dy):
                        count += 1
    
    return count

def solve_puzzle(input_text):
    grid = [list(line.strip()) for line in input_text.strip().splitlines() if line.strip()]
    return find_xmas(grid)

try:
    with open('4.txt', 'r') as file:
        puzzle_input = file.read()
    result = solve_puzzle(puzzle_input)
    print(f"Found {result} occurrences of XMAS in the word search")
except FileNotFoundError:
    print("Error: Could not find file '4.txt' in the current directory")
except Exception as e:
    print(f"An error occurred: {e}")
