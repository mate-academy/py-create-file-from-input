def main() -> None:
    filename_condition = True
    while filename_condition:
        filename = input("Enter name of the file: ")
        if filename:
            filename_condition = False

    content_condition = True
    content = ""
    while content_condition:
        content_line = input("Enter new line of content: ")

        if content_line == "stop":
            break
        content += content_line + "\n"

    with open(f"{filename}.txt", "w") as app:
        app.write(content)


if __name__ == "__main__":
    main()
