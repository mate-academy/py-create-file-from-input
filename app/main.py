def main() -> None:
    file_name = input("Enter name of the file: ")
    text_file = open(f"{file_name}", "w")
    text_file.write(f"File name: \"{file_name}.txt\"\nFile content: \n")
    text_file.close()
    while True:
        text = input("Enter new line of content: ")
        if text == "stop":
            break
        else:
            with open(f"{file_name}", "a") as text_file:
                text_file.write(f"{text}\n")


if __name__ == "__main__":
    main()
