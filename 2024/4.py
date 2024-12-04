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
    forward = ""
    for i in range(3):  # MAS is 3 characters
        new_x, new_y = x + i * dx, y + i * dy
        if not (0 <= new_x < rows and 0 <= new_y < cols):
            return False
        forward += grid[new_x][new_y]
    return forward in ["MAS", "SAM"]

def find_x_mas(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    
    # For each center point of potential X
    for i in range(1, rows-1):  # Need room for diagonal parts
        for j in range(1, cols-1):
            # Check all four possible combinations of X patterns:
            # 1. Both forward MAS
            # 2. Both backward SAM
            # 3. Upper-left to lower-right forward, other backward
            # 4. Upper-left to lower-right backward, other forward
            
            # Directions for the two lines of the X
            diagonals = [
                # upper-left to lower-right, upper-right to lower-left
                [(-1, -1), (1, 1)],  # First diagonal
                [(-1, 1), (1, -1)]   # Second diagonal
            ]
            
            # Check each diagonal pair
            for d1_start, d1_end in diagonals[0]:
                for d2_start, d2_end in diagonals[1]:
                    # Check if we can form valid MAS/SAM patterns in both diagonals
                    if (
                        (check_mas(grid, i+d1_start, j+d1_start, -d1_start, -d1_start) and
                         check_mas(grid, i+d2_start, j+d2_start, -d2_start, -d2_start))
                    ):
                        count += 1
                        break  # Found one valid X-MAS pattern, move to next center point
                    
    return count

def solve_puzzle(input_text):
    # Convert input text to grid
    grid = [list(line.strip()) for line in input_text.strip().splitlines() if line.strip()]
    
    # Solve both parts
    xmas_count = find_xmas(grid)
    x_mas_count = find_x_mas(grid)
    
    return xmas_count, x_mas_count

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
