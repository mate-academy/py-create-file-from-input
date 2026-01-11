def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    with open(file_name, "w") as open_file:
        while True:
            text = input("Enter new line of content: ") + "\n"
            if text == "stop" + "\n":
                break
            open_file.write(text)


if __name__ == "__main__":
    main()
