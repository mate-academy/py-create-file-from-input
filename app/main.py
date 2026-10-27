def main() -> None:
    name = input("Enter name of the file: ")
    content = []
    line = input("Enter new line of content: ")
    while line != "stop":
        content.append(line)
        line = input("Enter new line of content: ")

    file_name = f"{name}.txt"
    with open(file_name, "w") as file:
        file.write("\n".join(content))


if __name__ == "__main__":
    main()
