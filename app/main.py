def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "a") as file:
        while True:
            line_text = input("Enter new line of content: ")
            if line_text == "stop":
                break
            else:
                file.write(line_text + "\n")


if __name__ == "__main__":
    main()
