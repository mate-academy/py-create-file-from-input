def main() -> None:
    file_basename = input("Enter name of the file: ")
    filename = file_basename + ".txt"

    lines = []

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        lines.append(line)

    text_file = open(filename, "w")
    text_file.write("\n".join(lines))
    text_file.close()


if __name__ == "__main__":
    main()
