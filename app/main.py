def main() -> None:
    name_file = input("Enter name of the file: ") + ".txt"

    input_line = []

    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        input_line.append(line)

    with open(name_file, "w") as first_test:
        first_test.write("\n".join(input_line))


if __name__ == "__main__":
    main()
