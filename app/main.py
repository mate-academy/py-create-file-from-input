def main() -> None:
    file_name = input("Enter name of the file: ")
    file_content = []
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        file_content.append(line)

    file_path = f"{file_name}.txt"

    with open(file_path, "w") as file:
        for line in file_content:
            file.write(f"{line}\n")


if __name__ == "__main__":
    main()
