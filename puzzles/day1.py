def solve(input_file):
    with open(input_file, 'r') as f:
        data = [line.strip() for line in f.readlines()]
    # Your puzzle-solving logic here
    left_numbers = []
    right_numbers = []
    for line in data:
        left, right = map(int, line.split())
        left_numbers.append(left)
        right_numbers.append(right)
    left_numbers.sort()
    right_numbers.sort()
    result = 0
    for a,b in zip(left_numbers, right_numbers):
        result += abs(a-b)
    return result

def solvePart2(input_file):
    with open(input_file, 'r') as f:
        data = [line.strip() for line in f.readlines()]
    # Your puzzle-solving logic here
    left_numbers = []
    right_numbers = []
    for line in data:
        left, right = map(int, line.split())
        left_numbers.append(left)
        right_numbers.append(right)
    score = 0
    occurences  = {}
    for key in set(left_numbers):
        occurences[key] = right_numbers.count(key)

    for number in left_numbers:
        score += occurences[number] * number

    return score

if __name__ == "__main__":
    day = "day1"  # Change this for each day
    input_file = f'../input/{day}.txt'
    print(f"{day.capitalize()} Solution:", solve(input_file))
    print(f"{day.capitalize()} Solution:", solvePart2(input_file))

