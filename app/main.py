def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name += ".txt"
    lines = []

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        else:
            lines.append(line)

    output_file = open(file_name, "w")
    for line in lines:
        output_file.write(line + "\n")
    output_file.close()


if __name__ == "__main__":
    main()
