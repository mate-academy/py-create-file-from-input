def main() -> None:
    line_list = []

    filename = input("Enter name of the file: ") + ".txt"
    while True:
        line = input("Enter new line of content: ")
        if line != "stop":
            line_list.append(line)
        else:
            break

    with open(filename, "a") as f:
        for line in line_list:
            f.write(f"{line}\n")


if __name__ == "__main__":
    main()
