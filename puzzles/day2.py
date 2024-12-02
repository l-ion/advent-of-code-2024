def is_safe(report):
    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]
        if not (1 <= abs(diff) <= 3):
            return False
        if (report[i] < report[i + 1]) != (report[0] < report[1]):
            return False
    return True


def is_safe_with_one_removal(report):
    if is_safe(report):
        return True
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]
        if is_safe(modified_report):
            return True
    return False


def solve_part1(input_file):
    safe_count = 0
    with open(input_file, 'r') as file:
        for line in file:
            report = list(map(int, line.split()))
            if is_safe(report):
                safe_count += 1
    return safe_count


def solve_part2(input_file):
    safe_count = 0
    with open(input_file, 'r') as file:
        for line in file:
            report = list(map(int, line.split()))
            if is_safe_with_one_removal(report):
                safe_count += 1
    return safe_count

if __name__ == "__main__":
    day = "day2"  # Change this for each day
    input_file = f'../input/{day}.txt'
    print(f"{day.capitalize()} part 1 solution:", solve_part1(input_file))
    print(f"{day.capitalize()} part 2 solution:", solve_part2(input_file))




