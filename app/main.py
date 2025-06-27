def main() -> None:
    current_file = input(f"Enter name of the file: ") + ".txt"

    new_lines = []
    while True:
        new_line = input("Enter new line of content: ")
        if new_line.strip().lower() == "stop":
            break
        new_lines.append(new_line)

    with open(current_file, "w") as f:
        for line in new_lines:
            f.write(line + "\n")


if __name__ == "__main__":
    main()
