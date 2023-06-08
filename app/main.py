def main() -> None:
    file_name = input("Enter name of the file: ")
    text = ""
    with open(f"{file_name}.txt", "a") as text_file:
        while text != "stop":
            text = input("Enter new line of content: ")
            if text != "stop":
                text_file.write(text + "\n")


if __name__ == "__main__":
    main()
