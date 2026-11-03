def main() -> None:
    name = input("Enter name of the file: ").strip()

    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line.strip().lower() == "stop":
            break
        lines.append(line)

    with open(name + ".txt", "w") as output_file:
        for line in lines:
            output_file.write(line + "\n")


if __name__ == "__main__":
    main()
