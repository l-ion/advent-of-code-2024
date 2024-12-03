def solve_part1(input_file):
    with open(input_file, 'r') as file:
        for line in file:
            input = list(map(int, line.split()))
    return 0


def solve_part2(input_file):
    with open(input_file, 'r') as file:
        for line in file:
            input = list(map(int, line.split()))
    return 0

if __name__ == "__main__":
    day = "day3"  # Change this for each day
    input_file = f'../input/{day}.txt'
    print(f"{day.capitalize()} part 1 solution:", solve_part1(input_file))
    print(f"{day.capitalize()} part 2 solution:", solve_part2(input_file))




