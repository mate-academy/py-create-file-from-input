def main() -> None:
    input_file_name = input("Enter name of the file: ")
    text = ""
    while True:
        content_input = input("Enter new line of content: ")
        if "stop" in content_input:
            break
        text = f"{text}{content_input}\n"
    new_file = open(f"{input_file_name}.txt", "w")
    new_file.write(text)


if __name__ == "__main__":
    main()
