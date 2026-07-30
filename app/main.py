def main() -> None:
    file_name = input("Enter name of the file: ").strip()
    full_name = f"{file_name}.txt"

    lines = []

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        lines.append(line)

    with open(full_name, "w") as f:
        f.write("\n".join(lines))


if __name__ == "__main__":
    main()
