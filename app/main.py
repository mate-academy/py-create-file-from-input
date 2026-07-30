def main() -> None:
    file_name = input("Enter name of the file: ")
    file_content = []

    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        file_content.append(line)

    file_name += ".txt"

    with open(file_name, "w") as file:
        for line in file_content:
            file.write(line + "\n")

    print(f"File name: {file_name}")
    print("File content:")
    for line in file_content:
        print(line)


if __name__ == "__main__":
    main()
