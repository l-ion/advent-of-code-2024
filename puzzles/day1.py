def solve(input_file):
    with open(input_file, 'r') as f:
        data = f.readlines()
    # Your puzzle-solving logic here
    return data

if __name__ == "__main__":
    day = "day1"  # Change this for each day
    input_file = f'../input/{day}.txt'
    print(f"{day.capitalize()} Solution:", solve(input_file))
