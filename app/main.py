def main() -> None:
    file_name = input("Enter name of the file: ")

    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        lines.append(line)

    with open(f"{file_name}.txt", "w") as document:
        for line in lines:
            document.write(line + "\n")


if __name__ == "__main__":
    main()
