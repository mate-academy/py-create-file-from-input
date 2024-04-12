def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    content = []

    print("Enter lines of content (type 'stop' to finish):")
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content.append(line)

    with open(file_name, "w") as file:
        for line in content:
            file.write(line + "\n")

    print("File '{}' created successfully.".format(file_name))
    print("Content provided:")
    for line in content:
        print(line)


if __name__ == "__main__":
    main()
