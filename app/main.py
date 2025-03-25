def main() -> None:
    filename = input("Enter name of the file: ") + ".txt"

    lines = []
    writing = True
    while writing:
        new_line = input("Enter new line of content: ")
        if new_line.lower() == "stop":
            break
        lines.append(new_line)

    with open(filename, "w") as file:
        file.write("\n".join(lines))

    print(f'File name: "{filename}"')
    print("File content")
    for line in lines:
        print(line)


if __name__ == "__main__":
    main()
