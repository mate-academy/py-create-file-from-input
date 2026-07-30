def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name += ".txt"

    is_stopped = False
    content = ""

    while not is_stopped:
        line_of_content = input("Enter new line of content: ")
        if line_of_content == "stop":
            is_stopped = True
        else:
            content += f"{line_of_content}\n"

    open(file_name, "w").write(content)


if __name__ == "__main__":
    main()
