def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    lines_file = open(file_name, "a")
    while True:
        line = input("Enter new line of content: ") + "\n"
        if line == "stop\n":
            break
        lines_file.write(line)
    lines_file.close()


if __name__ == "__main__":
    main()
