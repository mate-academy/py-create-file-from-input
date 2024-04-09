def main() -> None:
    file_name = input("Enter name of the file: ")
    content = []
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content.append(line)
    file_with_extension = file_name + ".txt"
    with open(file_with_extension, "a") as file:
        for el in content:
            file.write(el + "\n")

        print(f"\nFile name: \"{file}\"")
        print("File content:")
        for line in content:
            print(line)


if __name__ == "__main__":
    main()
