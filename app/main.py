def main() -> None:
    file_name = input("Enter name of the file: ").strip()
    if not file_name.endswith(".txt"):
        file_name += ".txt"

    lines = []
    while True:
        line = input("Enter new line of content: ").strip()
        if line.lower() == "stop":
            break
        lines.append(line)

    with open(file_name, "w") as file:
        file.write("\n".join(lines))

    print(f"file '{file_name}' created successfully")


if __name__ == "__main__":
    main()
