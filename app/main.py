file_name = input("Enter file name:") + ".txt"

with open(file_name, "w") as file:
    while True:
        line = input("Write new line of content:")
        if line.lower() == "stop":
            break
        file.write(line + "\n")
