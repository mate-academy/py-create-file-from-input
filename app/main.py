def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    lines = []
    while True:
        line_input = input("Enter new line of content: ")

        if line_input == "stop":
            break

        lines.append(line_input)
    with open(file_name, "w") as file:
        file.write("\n".join(lines))


if __name__ == "__main__":
    main()
