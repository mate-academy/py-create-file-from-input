def main() -> None:
    file_name = input("Enter name of the file: ")
    if not file_name.endswith(".txt"):
        file_name += ".txt"

    content = []

    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            if not content:
                print("No content to write to the file.")
                break
            else:
                break
        content.append(line)

    if content:
        with open(file_name, "w") as file:
            for line in content:
                file.write(line + "\n")

    else:
        with open(file_name, "w"):
            pass

    print(f"\nFile name: {file_name}")
    print("File contents:")
    for line in content:
        print(line)

    print(f"\nFile {file_name} was successfully created")


if __name__ == "__main__":
    main()
