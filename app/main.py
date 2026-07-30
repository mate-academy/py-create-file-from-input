def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(file_name + ".txt", "w") as f:
        while True:
            text_for_file = input("Enter new line of content: ")
            if text_for_file == "stop":
                return
            f.write(text_for_file + "\n")


if __name__ == "__main__":
    main()
