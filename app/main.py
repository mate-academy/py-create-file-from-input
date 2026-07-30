def main() -> None:
    file_name = input("Enter name of the file: ")
    if not file_name.endswith(".txt"):
        file_name += ".txt"

    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        lines.append(line)

    with open(file_name, "w") as f:
        for line in lines:
            f.write(line + "\n")


if __name__ == "__main__":
    main()
