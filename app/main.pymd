file_name = input("Enter name of the file: ")

lines = []

while True:
    line = input("Enter new line of content: ")
    if line == "stop":
        break
    lines.append(line)

full_name = file_name + ".txt"

with open(full_name, "w") as f:
    for line in lines:
        f.write(line + "\n")
