def main() -> None:
    while True:
        file_name = input("Enter name of the file: ")
        if not file_name.strip():
            print("file name cannot be empty")
            continue
        if not file_name.endswith(".txt"):
            file_name += ".txt"
            break
    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        if not line.strip():
            print("Line can't be empty")
            continue
        lines.append(line)
    with open(file_name, "w") as file:
        for line in lines:
            file.write(line + "\n")
    print("File created")


if __name__ == "__main__":
    main()
