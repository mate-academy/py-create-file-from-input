def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    content = []
    input_value = input("Enter new line of content: ")
    while input_value != "stop":
        content.append(input_value)
        input_value = input("Enter new line of content: ")

    file_ = open(file_name, "w")
    file_.write("\n".join(content))
    file_.close()


if __name__ == "__main__":
    main()
