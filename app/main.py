def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name += ".txt"
    stream = open(file_name, "w")
    content = []
    while True:
        command = input("Enter new line of content: ")
        if command == "stop":
            break
        content.append(command)
    for elem in content:
        stream.write(f"{elem}\n")
    stream.close()


if __name__ == "__main__":
    main()
