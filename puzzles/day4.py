xmas_count = 0
input_file = f'../input/day4.txt'
data = open(input_file, 'r').read().split("\n")

for i in range(len(data)):
    for j in range (len(data[i])):
        if data[i][j] == "X":
            # check right
            if (i + 3) <= (len(data) - 1):
                if data[i+1][j] == "M" and data[i+2][j] == "A" and data[i+3][j] == "S":
                    xmas_count += 1
            # check left
            if (i - 3) >= 0:
                if data[i-1][j] == "M" and data[i-2][j] == "A" and data[i-3][j] == "S":
                    xmas_count += 1
            # check up
            if (j + 3) <= (len(data[i]) - 1):
                if data[i][j+1] == "M" and data[i][j+2] == "A" and data[i][j+3] == "S":
                    xmas_count += 1
            # check down
            if (j - 3) >= 0:
                if data[i][j-1] == "M" and data[i][j-2] == "A" and data[i][j-3] == "S":
                    xmas_count += 1
            # check diagonal down right
            if i + 3 <= (len(data) - 1) and (j + 3) <= (len(data[i]) - 1):
                if data[i+1][j+1] == "M" and data[i+2][j+2] == "A" and data[i+3][j+3] == "S":
                    xmas_count += 1
            # check diagonal down left
            if i + 3 <= (len(data) - 1) and (j - 3) >= 0:
                if data[i+1][j-1] == "M" and data[i+2][j-2] == "A" and data[i+3][j-3] == "S":
                    xmas_count += 1
            # check diagonal up right
            if i - 3 >= 0 and (j + 3) <= (len(data[i]) - 1):
                if data[i-1][j+1] == "M" and data[i-2][j+2] == "A" and data[i-3][j+3] == "S":
                    xmas_count += 1
            # check diagonal up left
            if i - 3 >= 0 and (j - 3) >= 0:
                if data[i-1][j-1] == "M" and data[i-2][j-2] == "A" and data[i-3][j-3] == "S":
                    xmas_count += 1

x_mas_count = 0

def index_exists(data, i, j):
    return 0 <= i < len(data) and 0 <= j < len(data[i])

for i in range(len(data)):
    for j in range (len(data[i])):
        if data[i][j] == "A" and index_exists(data, i-1, j-1) and data[i-1][j-1] == "M" and index_exists(data, i+1, j+1) and data[i+1][j+1] == "S" and index_exists(data, i-1, j+1) and data[i-1][j+1] == "S" and index_exists(data, i+1, j-1) and data[i+1][j-1] == "M":
            x_mas_count += 1
        if data[i][j] == "A" and index_exists(data, i-1, j-1) and data[i-1][j-1] == "S" and index_exists(data, i+1, j+1) and data[i+1][j+1] == "M" and index_exists(data, i-1, j+1) and data[i-1][j+1] == "M" and index_exists(data, i+1, j-1) and data[i+1][j-1] == "S":
            x_mas_count += 1
        if data[i][j] == "A" and index_exists(data, i-1, j-1) and data[i-1][j-1] == "M" and index_exists(data, i+1, j+1) and data[i+1][j+1] == "S" and index_exists(data, i-1, j+1) and data[i-1][j+1] == "M" and index_exists(data, i+1, j-1) and data[i+1][j-1] == "S":
            x_mas_count += 1
        if data[i][j] == "A" and index_exists(data, i-1, j-1) and data[i-1][j-1] == "S" and index_exists(data, i+1, j+1) and data[i+1][j+1] == "M" and index_exists(data, i-1, j+1) and data[i-1][j+1] == "S" and index_exists(data, i+1, j-1) and data[i+1][j-1] == "M":
            x_mas_count += 1


if __name__ == "__main__":
    print(f"Part1: {xmas_count}")
    print(f"Part2: {x_mas_count}")

