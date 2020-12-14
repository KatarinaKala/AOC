with open("1ainput.txt", "r") as file:
    lines = [int(line) for line in file.read().split("\n")]

for i, num in enumerate(lines):
    for j in range(i+1, len(lines)):
        if num + lines[j] == 2020:
            print(f"Answer is: {num * lines[j]}")
            break
