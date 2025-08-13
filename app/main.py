def main() -> None:
    file_name = input("Enter name of the file: ")
    stop = False

    if not file_name.endswith(".txt"):
        file_name += ".txt"

    while not stop:
        content = input("Enter new line of content: ")
        if content.lower() == "stop":
            stop = True
        else:
            content += "\n"
            with open(file_name, "a") as output_file:
                output_file.write(content)


if __name__ == "__main__":
    main()
