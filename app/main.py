def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    with open(file_name, "a") as f:
        stop = "stop"
        while True:
            text_line = input("Enter new line of content: ")
            if text_line == stop:
                break

            f.write(text_line + "\n")


if __name__ == "__main__":
    main()
