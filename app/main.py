def main() -> None:
    file_name = input("Enter name of the file: ").strip()
    if not file_name.endswith(".txt"):
        file_name += ".txt"

    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line.strip().lower() == "stop":
            break
        lines.append(line)

    with open(file_name, "w") as f:
        f.write("\n".join(lines))
    print(f'File name: "{file_name}"')
    print("File content:")
    for line in lines:
        print(line)


if __name__ == "__main__":
    main()
