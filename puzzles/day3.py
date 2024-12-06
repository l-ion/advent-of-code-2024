import re

input_file = f'../input/day3.txt'
data = open(input_file, 'r').read()

result = 0
resultWithFlags = 0
enabled = True

regex = r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))"

matches = re.findall(regex, data)

for a, b, do, donot in matches:
    if do or donot:
        enabled = bool(do)
    else:
        multiply = int(a) * int(b)
        result += multiply
        resultWithFlags += multiply * enabled

if __name__ == "__main__":
    print(f"Part1: {result}")
    print(f"Part2: {resultWithFlags}")
