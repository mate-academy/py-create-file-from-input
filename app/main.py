def main() -> None:
    name = input("Enter name of the file: ")
    name += ".txt"

    line = []

    while True:
        input_line = input("Enter new line of content: ")
        if input_line == "stop":
            break
        line.append(input_line)

    with open(name, "w") as result_file:
        result_file.write("\n".join(line))


if __name__ == "__main__":
    main()
