# read_from_file.py

def read_from_file():
    file_name = input("Enter name of the file: ") + ".txt"
    content = []

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        content.append(line)

    with open(file_name, "w") as f:
        for line in content:
            f.write(line + "\n")


if __name__ == "__main__":
    read_from_file()
