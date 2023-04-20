def main() -> None:
    lines = []
    file_name = input("Enter name of the file: ")
    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        lines.append(line)
    with open(f"{file_name}.txt", "w") as doc:
        doc.write("\n".join(lines))


if __name__ == "__main__":
    main()
