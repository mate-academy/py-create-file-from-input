def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name += ".txt"
    with open(file_name, "a") as f:
        while True:
            new_line_content = input("Enter new line of content: ")
            if new_line_content == "stop":
                break
            f.write(new_line_content + "\n")


if __name__ == "__main__":
    main()
