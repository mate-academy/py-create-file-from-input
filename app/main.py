def main()-> None:
    file_name = input("Enter name of the file: ")
    file_name += ".txt"
    text = ""
    while True:
        text = input("Enter new line of content: ")
        with open(file_name, "a") as file:
            if text == "stop":
                return
            file.write(f"{text}\n")


if __name__ == "__main__":
    main()
