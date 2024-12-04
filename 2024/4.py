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

def check_mas(grid, x, y, dx, dy):
    """Check if 'MAS' or 'SAM' exists starting from (x,y) in direction (dx,dy)"""
    rows, cols = len(grid), len(grid[0])
    word = ""
    for i in range(3):  # MAS is 3 characters
        new_x, new_y = x + i * dx, y + i * dy
        if not (0 <= new_x < rows and 0 <= new_y < cols):
            return False
        word += grid[new_x][new_y]
    return word in ["MAS", "SAM"]

def find_x_mas(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    
    # For each potential center point
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            # Check for X pattern
            # First diagonal: upper-left to lower-right
            # Second diagonal: upper-right to lower-left
            
            # Try all combinations for the X pattern
            found = False
            for ul_forward in [True, False]:  # upper-left to lower-right can be forward or backward
                for ur_forward in [True, False]:  # upper-right to lower-left can be forward or backward
                    # Check upper-left to lower-right diagonal
                    ul_valid = check_mas(grid, i-1, j-1, 1, 1) if ul_forward else check_mas(grid, i+1, j+1, -1, -1)
                    
                    # Check upper-right to lower-left diagonal
                    ur_valid = check_mas(grid, i-1, j+1, 1, -1) if ur_forward else check_mas(grid, i+1, j-1, -1, 1)
                    
                    if ul_valid and ur_valid:
                        found = True
                        break
                if found:
                    break
            
            if found:
                count += 1
    
    return count

def solve_puzzle(input_text):
    # Convert input text to grid
    grid = [list(line.strip()) for line in input_text.strip().splitlines() if line.strip()]
    
    # Solve both parts
    xmas_count = find_xmas(grid)
    x_mas_count = find_x_mas(grid)
    
    return xmas_count, x_mas_count

# Read from file and solve
try:
    with open('4.txt', 'r') as file:
        puzzle_input = file.read()
    xmas_result, x_mas_result = solve_puzzle(puzzle_input)
    print(f"Part 1: Found {xmas_result} occurrences of XMAS in the word search")
    print(f"Part 2: Found {x_mas_result} X-MAS patterns in the word search")
except FileNotFoundError:
    print("Error: Could not find file '4.txt' in the current directory")
except Exception as e:
    print(f"An error occurred: {e}")
