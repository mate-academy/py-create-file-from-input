def main() -> None:
    user_input = input("Enter name of the file: ")

    lines = []

    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        lines.append(line)

    file_name = user_input + ".txt"
    with open(file_name, "w") as f:
        for line in lines:
            f.write(line + "\n")


if __name__ == "__main__":
    main()
