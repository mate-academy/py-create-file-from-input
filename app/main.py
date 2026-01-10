def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    with open(file_name, "a") as data_file:
        file_stop = False
        while not file_stop:
            text = input("Enter new line of content: ")
            if text == "stop":
                file_stop = True
            else:
                data_file.write(text + "\n")


if __name__ == "__main__":
    main()
