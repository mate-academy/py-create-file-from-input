def main() -> None:
    filename = input("Enter name of the file: ")
    if filename:
        content = ""
        content_line = ""
        while content_line != "stop":
            content_line = input("Enter new line of content: ")
            if content_line != "stop":
                content += content_line + "\n"

        user_file = open(filename + ".txt", "w")
        user_file.write(content)
        user_file.close()


if __name__ == "__main__":
    main()
