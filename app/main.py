file_name = input("Enter name of the file:")

with open(f"{file_name}.txt", "w") as f:
    line = ""
    while line != "stop":
        line = input("Enter new line of content:")
        f.write(f"{line}\n")
