def main() -> None:
    file_name = input("Enter name of the file: ")

    if not file_name.endswith(".txt"):
        file_name += ".txt"

    file_contents = ""

    while True:
        line = input("Enter new line of content: ")
        if line == "stop":
            break
        file_contents += line + "\n"

    output_file = open(file_name, "w")
    output_file.write(file_contents)
    output_file.close()


if __name__ == "__main__":
    main()
