def main() -> None:
    file_name = input("Enter name of the file: ")
    text_file = open(f"{file_name}.txt", "w")

    try:
        while True:
            text = input("Enter new line of content: ")

            if text == "stop":
                break
            text_file.write(text + "\n")
    finally:
        text_file.close()


if __name__ == "__main__":
    main()
