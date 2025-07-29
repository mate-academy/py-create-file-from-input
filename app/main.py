def main() -> None:
    file_name_input = input("Enter name of the file: ")
    file_name = file_name_input + ".txt"
    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        lines.append(line)
    with open(file_name, "w") as file:
        for line in lines:
            file.write(line + "\n")
    print(f"File name: \"{file_name}\"")
    print("File content:")
    for line in lines:
        print(line)


if __name__ == "__main__":
    main()
