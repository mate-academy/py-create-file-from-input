def main() -> None:
    file_name = input("Enter name of the file: ")
    lines = []

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        else:
            lines.append(line)

    with open(f"{file_name}.txt", "w") as f:
        text = "\n".join(lines)
        f.write(text)


if __name__ == "__main__":
    main()
