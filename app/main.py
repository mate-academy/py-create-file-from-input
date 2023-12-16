def main() -> None:
    filename = input("Enter name of the file: ")
    if not filename.endswith(".txt"):
        filename = filename + ".txt"
    buffer = []
    while True:
        input_line = input("Enter new line of content: ")
        if input_line == "stop":
            break
        buffer.append(input_line)
    with open(filename, "w") as f:
        [f.write(line + "\n") for line in buffer]


if __name__ == "__main__":
    main()
