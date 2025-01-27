def main() -> None:
    name_of_file = input("Enter name of the file: ") + ".txt"

    with open(name_of_file, "a") as f:
        while True:
            new_line_of_content = input("Enter new line of content: ")
            if new_line_of_content.lower() == "stop":
                break
            f.write(new_line_of_content + "\n")


if __name__ == "__main__":
    main()
