def main() -> None:
    name_file = input("Enter name of the file: ")
    line_file = ""
    body_file = []
    while True:
        line_file = input("Enter new line of content: ")
        if line_file == "stop":
            break
        body_file.append(line_file)

    with open(name_file + ".txt", "w") as f:
        for line in body_file:
            f.write(line + "\n")


if __name__ == "__main__":
    main()
