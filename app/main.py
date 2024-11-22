def main() -> None:
    name = input("Enter name of the file: ")
    name = name + ".txt"
    line = ""
    lines = []
    while line != "stop":
        line = input("Enter new line of content: ")
        if line != "stop":
            lines.append(line)
    input_file = open(name, "w")
    for line in lines:
        input_file.write(line)
        input_file.write("\n")
    input_file.close()


if __name__ == "__main__":
    main()
