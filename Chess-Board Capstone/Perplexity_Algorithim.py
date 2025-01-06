import matplotlib.pyplot as plt
import numpy as np
from collections import deque

# Define the knight's possible L-shaped moves
knight_moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

def is_valid_move(x, y, board):
    """Check if a move is within bounds and lands on an empty square."""
    return 0 <= x < 8 and 0 <= y < 8 and board[x, y] == 0

def find_optimized_knight_path(board, start, end):
    """Find an optimized path for the knight considering obstacles."""
    queue = deque([(start, [start], board.copy(), 0)])  # (current position, path, board state, cost)
    visited = set()

    best_path = None
    best_cost = float('inf')

    while queue:
        current, path, curr_board, cost = queue.popleft()

        # If we reach the end with an L-shaped move
        if current == end and len(path) > 1 and is_knight_move(path[-2], current):
            if cost < best_cost:
                best_path = path
                best_cost = cost
            continue

        if current in visited:
            continue
        visited.add(current)

        # Explore all possible moves
        for dx, dy in knight_moves:
            next_x = current[0] + dx
            next_y = current[1] + dy

            if is_valid_move(next_x, next_y, curr_board):
                new_board = curr_board.copy()
                queue.append(((next_x, next_y), path + [(next_x, next_y)], new_board, cost + 1))

            # Handle obstacles
            elif 0 <= next_x < 8 and 0 <= next_y < 8 and curr_board[next_x][next_y] == 1:
                # Temporarily move obstacle to a nearby empty square
                temp_pos = find_nearest_empty_square(curr_board, (next_x, next_y))
                if temp_pos:
                    new_board = curr_board.copy()
                    new_board[next_x][next_y] = 0  # Clear obstacle
                    new_board[temp_pos[0]][temp_pos[1]] = 1  # Move obstacle
                    queue.append(((next_x, next_y), path + [(next_x, next_y)], new_board, cost + 10))  # Higher cost for moving pieces

    return best_path

def is_knight_move(start, end):
    """Check if a move is an L-shaped knight move."""
    dx = abs(start[0] - end[0])
    dy = abs(start[1] - end[1])
    return (dx == 2 and dy == 1) or (dx == 1 and dy == 2)

def find_nearest_empty_square(board, pos):
    """Find the nearest empty square to temporarily move an obstacle."""
    queue = deque([pos])
    visited = set()

    while queue:
        current = queue.popleft()
        if current in visited:
            continue
        visited.add(current)

        x, y = current
        if board[x][y] == 0:  # Found an empty square
            return current

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 8 and 0 <= ny < 8 and (nx, ny) not in visited:
                queue.append((nx, ny))

    return None

def visualize_board(board, path):
    """Visualize the board and the knight's movement."""
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.imshow(board.T, cmap="gray_r", origin="lower")

    # Plot the path
    for i in range(len(path) - 1):
        x1, y1 = path[i]
        x2, y2 = path[i + 1]
        ax.plot([y1, y2], [x1, x2], color="blue", linewidth=2)

    # Mark start and end positions
    ax.text(path[0][1], path[0][0], "S", color="green", ha="center", va="center", fontsize=16)
    ax.text(path[-1][1], path[-1][0], "E", color="red", ha="center", va="center", fontsize=16)

    plt.show()

# Test case: Board with obstacles
board = np.zeros((8, 8))
board[5][5] = board[4][6] = board[3][5] = board[3][3] = board[6][4] = board[6][6] = 1

start = (4, 4)
end = (6, 5)

path = find_optimized_knight_path(board.copy(), start, end)
print("Optimized Path:", path)
visualize_board(board.copy(), path)