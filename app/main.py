def main() -> None:
    lines = []

    file_name = input("Enter name of the file: ").strip() + ".txt"

    while True:

        new_line = input("Enter new line of content: ").strip()
        if new_line.lower() == "stop":
            break
        lines.append(new_line)

    with open(file_name, "w") as new_file:
        for line in lines:
            new_file.write(line + "\n")

    print(f"File '{file_name}' created with the provided content.")


if __name__ == "__main__":
    main()
