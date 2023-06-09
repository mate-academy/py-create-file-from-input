def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    file_content = []

    while True:
        next_line = input("Enter new line of content: ")

        if next_line.lower() == "stop":
            break

        file_content.append(next_line)

    with open(file_name, "w") as f:
        for line in file_content:
            f.write(line + "\n")

    print(f"File '{file_name}' has been created with the provided content.")


if __name__ == "__main__":
    main()
