def main() -> None:
    file_name = input("Enter name of the file: ")
    file_content = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        file_content.append(line)

    file_path = file_name + ".txt"
    with open(file_path, "w") as file:
        for line in file_content:
            file.write(line + "\n")

    print(f"File name: {file_path}")
    print("File content:")
    with open(file_path, "r") as file:
        print(file.read())


if __name__ == "__main__":
    main()
