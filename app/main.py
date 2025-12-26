def main() -> None:
    file_name = input("Enter name of the file: ")
    file_lines = []
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        file_lines.append(line)
    file_content = "\n".join(file_lines)

    with open(f"{file_name}.txt", "w") as f:
        f.write(file_content)
        print(f'\nFile name: "{file_name}.txt"')
        print("File content:")
        print(file_content)


if __name__ == "__main__":
    main()
