file_name = input("Please, enter File name : ")

lines = []
line = ""
while line != "stop":
    line = input("Enter new line of content: ")
    lines.append(line)

with open(f"{file_name}.txt", "w", encoding="utf8") as file:
    for line in lines:
        file.write(f"{line}\n")
    print(f"Recording file - {file_name}.txt - is success")
