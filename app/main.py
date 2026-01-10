def main() -> str:
    file_name = input("Enter name of the file: ")
    file_name += ".txt"
    content_lines = []
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)
    with open(file_name, "w") as file:
        for line in content_lines:
            file.write(line + "\n")

    print(f"\nFile name: '{file_name}'")
    print("File content:")
    for line in content_lines:
        print(f"# {line}")


if __name__ == "__main__":
    main()
