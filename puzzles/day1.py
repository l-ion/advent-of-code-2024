def solvePart1(input_file):
    with open(input_file, 'r') as f:
        data = [line.strip() for line in f.readlines()]
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
    left_numbers = []
    right_numbers = []
    for line in data:
        left, right = map(int, line.split())
        left_numbers.append(left)
        right_numbers.append(right)
    similarityScore = 0
    occurrences = {}
    for key in set(left_numbers):
        occurrences[key] = right_numbers.count(key)

    for number in left_numbers:
        similarityScore += occurrences[number] * number

    return similarityScore

if __name__ == "__main__":
    day = "day1"  # Change this for each day
    input_file = f'../input/{day}.txt'
    print(f"{day.capitalize()} part 1 solution:", solvePart1(input_file))
    print(f"{day.capitalize()} part 2 Solution:", solvePart2(input_file))

