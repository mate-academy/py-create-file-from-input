def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name += ".txt"

    lines_to_append = []
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        lines_to_append.append(line)

    with open(file_name, "w") as f:
        for line in lines_to_append:
            f.write(line + "\n")


if __name__ == "__main__":
    main()
