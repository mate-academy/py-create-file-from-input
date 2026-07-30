def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name += ".txt"
    with open(file_name, "a") as file:
        while True:
            text_content = input("Enter new line of content: ")
            if text_content != "stop":
                file.write(text_content)
                file.write("\n")
            else:
                break


if __name__ == "__main__":
    main()
