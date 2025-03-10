def main() -> None:
    file_name = input("Enter name of the file: ")
    content = []
    while True:
        next_line = input("Enter new line of content: ")
        if next_line == "stop":
            break
        content.append(next_line + "\n")

    with open(f"{file_name}.txt", "w") as file:
        for line in content:
            file.write(line)


if __name__ == "__main__":
    main()
