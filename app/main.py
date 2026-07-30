def main() -> None:
    filename = input("Enter name of the file: ")
    filename = filename + ".txt"

    lines = []

    while True:
        user_input = input("Enter new line of content: ")
        if user_input == "stop":
            break
        lines.append(user_input)

    with open(filename, "w") as f:
        for line in lines:
            f.write(line + "\n")


if __name__ == "__main__":
    main()
