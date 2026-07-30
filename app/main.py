def main() -> any:

    is_finished = False
    file_name = input("Enter name of the file: ")
    content_list = []

    while not is_finished:
        content_line = input("Enter new line of content: ")
        if content_line == "stop":
            is_finished = True
        else:
            content_list.append(content_line)

    with open(f"{file_name}.txt",
              mode="w",
              encoding="utf-8",
              newline=""
              ) as f:
        for line in content_list:
            f.write(f"{line}\n")


if __name__ == "__main__":
    main()
