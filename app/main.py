file = ""

while len(file) == 0:
    file = input("Enter name of the file: ")
    file = file.strip()

if ".txt" not in file:
    file += ".txt"

with open(file, "w") as f:
    while True:
        content = input("Enter new line of content: ")
        if content == "stop":
            break
        f.write(content + "\n")
    f.close()
