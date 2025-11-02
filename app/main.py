def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    lines = []
    line = ""
    print("Enter file content (type \'stop\' to end the file):")
    while line != "stop":
        line = input("Enter new line of content: ")
        lines.append(line) if line != "stop" else None
    text_file = open(file_name, "w")
    for line in lines:
        text_file.write(f"{line}\n")
    text_file.close()


if __name__ == "__main__":
    main()
