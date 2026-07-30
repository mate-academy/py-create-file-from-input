def main() -> None:
    file_name = input("Enter name of the file: ")
    lines = []
    line = input("Enter new line of content: ")
    while line.lower() != "stop":
        lines.append(line)
        line = input("Enter new line of content: ")
    with open(f"{file_name}.txt", "a") as f:
        for line in lines:
            f.write(f"{line}\n")


if __name__ == "__main__":
    main()
