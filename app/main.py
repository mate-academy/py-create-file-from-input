file_name = input("Enter name of the file: ") + ".txt"
lines_list = []

while True:
    content = input("Enter new line of content:")
    if content == "stop":
        break
    lines_list.append(content)

with open(file_name, "x") as file:
    for line in lines_list:
        file.write(line + "\n")
