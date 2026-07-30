def main() -> None:
    stop_word = "stop"
    content = []

    name_of_the_file = input("Enter name of the file: ")

    # content loop
    while True:
        content_line = input("Enter new line of content: ")
        if content_line == stop_word:
            break
        else:
            content.append(content_line)

    with open(f"{name_of_the_file}.txt", "w", encoding="utf-8") as file_obj:
        file_obj.write("\n".join(content))


if __name__ == "__main__":
    main()
