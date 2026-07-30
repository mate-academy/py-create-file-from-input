def main() -> None:
    filename = input("Enter name of the file: ")
    if filename[-4:] != ".txt":
        filename += ".txt"
    output_file = open(filename, "w")
    lines = []
    newline = ""
    while newline != ("stop" + "\n"):
        lines.append(newline)
        newline = input("Enter new line of content: ") + "\n"
    output_file.writelines(lines)
    output_file.close()


if __name__ == "__main__":
    main()
