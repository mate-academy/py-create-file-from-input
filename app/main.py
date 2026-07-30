def main() -> None:
    lines = []
    file_name = input("Enter name of the file: ")
    if not file_name.endswith(".txt"):
        file_name += ".txt"

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        lines.append(line)

    new_file = open(file_name, "w")
    for line in lines:
        new_file.write(line + "\n")
    new_file.close()


if __name__ == "__main__":
    main()
