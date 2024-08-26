"""
 The Flood Fill Algorithm is commonly used in computer graphics to determine the area connected 
 to a given node in a multi-dimensional array (like an image).
"""

class FloodFill:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0

    def is_valid(self, x, y, target_color):
        return (0 <= x < self.rows and 
                0 <= y < self.cols and 
                self.grid[x][y] == target_color)

    def fill(self, x, y, new_color):  # The main method that is needed to be called.
        target_color = self.grid[x][y]
        if target_color == new_color:
            return
        
        self._flood_fill(x, y, target_color, new_color)

    def _flood_fill(self, x, y, target_color, new_color):
        if not self.is_valid(x, y, target_color):
            return
        
        self.grid[x][y] = new_color

        # Recursively fill adjacent pixels (up, down, left, right)
        self._flood_fill(x + 1, y, target_color, new_color)  # Down
        self._flood_fill(x - 1, y, target_color, new_color)  # Up
        self._flood_fill(x, y + 1, target_color, new_color)  # Right
        self._flood_fill(x, y - 1, target_color, new_color)  # Left

    def get_grid(self):
        return self.grid


# Example Usage
initial_grid = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

flood_fill = FloodFill(initial_grid)
print("Initial Grid:")
for row in flood_fill.get_grid():
    print(row)

# Apply flood fill starting at (1, 1) with new color 2
flood_fill.fill(1, 1, 2)

print("\nGrid After Flood Fill:")
for row in flood_fill.get_grid():
    print(row)


"""
Explanation of the Code:-

>>FloodFill Class:
-Initializes with a given grid, which represents the initial state of the area.
-Contains methods to check if a cell is valid and to perform the flood fill.

>>is_valid Method:
-Checks if the given coordinates (x, y) are within bounds and match the target_color.

>>fill Method:
-Initiates the flood fill process by calling the recursive _flood_fill method.

>>_flood_fill Method:
-Changes the color of the current cell and recursively calls itself for adjacent cells (up, down, left, right).

>>get_grid Method:
-Returns the updated grid after the flood fill.

Example Output:-

Given the initial grid:
[1, 1, 0, 0, 0]
[1, 1, 0, 1, 1]
[0, 0, 0, 1, 0]
[0, 1, 1, 1, 0]
[0, 0, 0, 0, 0]

After applying flood fill starting at (1, 1) with a new color of 2, the updated grid will look like:

[2, 2, 0, 0, 0]
[2, 2, 0, 1, 1]
[0, 0, 0, 1, 0]
[0, 1, 1, 1, 0]
[0, 0, 0, 0, 0]

This implementation effectively demonstrates the flood fill algorithm in action!
"""

