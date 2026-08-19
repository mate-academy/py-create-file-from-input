def main() -> None:
    name_of_file = input("Enter name of the file: ")
    content = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        content.append(line)
    with open(f"{name_of_file}.txt", "w") as file:
        file.write("\n".join(content))


if __name__ == "__main__":
    main()
