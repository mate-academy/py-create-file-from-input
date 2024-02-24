def main() -> None:
    name_of_file = input("Enter name of the file: ") + ".txt"
    with open(name_of_file, "w") as file:
        while True:
            line_of_content = input("Enter new line of content: ")
            if line_of_content.lower() == "stop":
                break
            file.write(line_of_content + "\n")


if __name__ == "__main__":
    main()
