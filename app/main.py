def main() -> None:
    file_name = input("Enter name of the file: ").strip()
    full_file_name = f"{file_name}.txt"

    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        lines.append(line)

    with open(full_file_name, "w") as file:
        for line in lines:
            file.write(line + "\n")
    pass


if __name__ == "__main__":
    main()
