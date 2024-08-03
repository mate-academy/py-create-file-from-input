def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "w") as text_file:
        while True:
            input_content = input("Enter new line of content: ")
            if input_content == "stop":
                break

            text_file.write(input_content + "\n")


if __name__ == "__main__":
    main()
