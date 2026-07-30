def main() -> None:
    filename = input("Enter name of the file: ")
    filename += ".txt"
    lines = []
    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        lines.append(line)
    write_file = open(filename, "w")
    write_file.write("\n".join(lines))
    write_file.close()


if __name__ == "__main__":
    main()
