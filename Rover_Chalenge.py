class Rover:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def find_intersections(input_file):
    rovers = set()
    intersection_points = set()
    plateau_x, plateau_y = 0, 0
    terrain = []  # 2D grid to represent terrain

    with open(input_file, 'r') as f:
        plateau_x, plateau_y = map(int, f.readline().split())
        terrain = [['.' for _ in range(plateau_x + 1)] for _ in range(plateau_y + 1)]
        
        while True:
            line = f.readline().strip()
            if not line:
                break
                
            initial_x, initial_y = map(int, line.split())
            instructions = f.readline().strip()
            
            rover = Rover(initial_x, initial_y)
            for move in instructions:
                if (rover.x, rover.y) in rovers:
                    intersection_points.add((rover.x, rover.y))
                    terrain[rover.y][rover.x] = '*'
                else:
                    rovers.add((rover.x, rover.y))
                    
                if move == 'N':
                    rover.y += 1
                    terrain[rover.y][rover.x] = '|'
                elif move == 'S':
                    rover.y -= 1
                    terrain[rover.y][rover.x] = '|'
                elif move == 'E':
                    rover.x += 1
                    terrain[rover.y][rover.x] = '-'
                elif move == 'W':
                    rover.x -= 1
                    terrain[rover.y][rover.x] = '-'

    return intersection_points, terrain

def print_terrain(terrain):
    for row in terrain:
        print(''.join(row))

def main():
    input_file = 'input.txt'
    intersection_points, terrain = find_intersections(input_file)

    print("Intersections")
    for i, point in enumerate(intersection_points, start=1):
        print(f"Intersection point {i}: {point[0]} {point[1]}")

    print("Visual representation Paths")
    print_terrain(terrain)

if __name__ == "__main__":
    main()
