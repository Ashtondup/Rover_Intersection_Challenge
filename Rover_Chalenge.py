class Rover:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def find_intersections(input_file):
    rovers = set()
    intersection_points = set()

    with open(input_file, 'r') as f:
        plateau_x, plateau_y = map(int, f.readline().split())
        print("Plateau:", plateau_x, plateau_y)
        
        while True:
            line = f.readline().strip()
            if not line:
                break
                
            initial_x, initial_y = map(int, line.split())
            print("Initial position:", initial_x, initial_y)
            
            instructions = f.readline().strip()
            print("Instructions:", instructions)
            
            rover = Rover(initial_x, initial_y)
            for move in instructions:

                if move == 'N':
                    rover.y += 1
                elif move == 'S':
                    rover.y -= 1
                elif move == 'E':
                    rover.x += 1
                elif move == 'W':
                    rover.x -= 1

                if (rover.x, rover.y) in rovers:
                    intersection_points.add((rover.x, rover.y))
                else:
                    rovers.add((rover.x, rover.y))

    return intersection_points

def main():
    input_file = 'input.txt'
    intersection_points = find_intersections(input_file)

    print("Intersections")
    for i, point in enumerate(intersection_points, start=1):
        print(f"Intersection point {i}: {point[0]} {point[1]}")

if __name__ == "__main__":
    main()
