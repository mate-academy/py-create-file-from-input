def main() -> None:
    file_name = input("Enter name of the file: ").strip()
    full_name = file_name + ".txt"
    lines = []

    while True:
        line = input("Enter new line of content: ").strip()
        if line == "stop":
            break
        lines.append(line)

    with open(full_name, "w") as file:
        for line in lines:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
