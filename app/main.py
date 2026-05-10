def main() -> None:
    name_of_file = input("Enter name of the file: ")
    filename = f"{name_of_file}.txt"
    content = []
    while True:
        new_line = input("Enter new line of content: ")
        if new_line == "stop":
            break
        content.append(new_line)
    with open(filename, "w") as file:
        file.write("\n".join(content))


if __name__ == "__main__":
    main()
