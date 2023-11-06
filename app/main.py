def main() -> None:
    file_name = input("Enter name of the file: ")

    with open(file_name + ".txt", "w") as file:
        while True:
            line_content = input("Enter new line of content: ")

            if line_content == "stop":
                break
            file.write(line_content + "\n")


if __name__ == "__main__":
    main()
