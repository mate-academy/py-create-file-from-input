def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    new_content = []

    while True:
        line_of_content = input("Enter new line of content: ")
        if line_of_content == "stop":
            break
        new_content.append(line_of_content)

    with open(file_name, "w") as f:
        for line in new_content:
            f.write(line + "\n")


if __name__ == "__main__":
    main()
