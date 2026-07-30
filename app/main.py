def main() -> None:
    with open(input("Enter name of the file: ") + ".txt", "w") as new_file:
        while True:
            content_line = input("Enter new line of content: ")
            if content_line == "stop":
                break
            new_file.write(content_line + "\n")


if __name__ == "__main__":
    main()
