def main() -> None:
    file_name = input("Enter name of the file: ")
    content = []
    line = ""
    while line != "stop":
        line = input("Enter new line of content: ")
        if line != "stop":
            content.append(line)
    with open(f"{file_name}.txt", "w") as file:
        file.write("\n".join(content))


if __name__ == "__main__":
    main()
