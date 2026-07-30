def main() -> None:
    file_name = input("Enter name of the file: ")
    lines = []

    while True:
        next_line = input("Enter new line of content: ")
        if next_line == "stop":
            break

        lines.append(next_line)

    with open(f"{file_name}.txt", "w") as f:
        f.write("\n".join(lines))


if __name__ == "__main__":
    main()
