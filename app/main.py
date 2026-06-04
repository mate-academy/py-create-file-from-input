def main() -> None:
    name = input("Enter name of the file: ") + ".txt"
    line_list = []

    while True:
        new_line = input("Enter new line of content: ")
        if new_line == "stop":
            break
        line_list.append(new_line)
    with open(name, "w") as f:
        for line in line_list:
            f.write(line + "\n")


if __name__ == "__main__":
    main()
