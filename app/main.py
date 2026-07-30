def main() -> None:
    while True:
        name = input("Enter name of the file: ")
        if name:
            file_name = name + ".txt"
            break
    with open(file_name, "a") as file:
        while True:
            text = input("Enter new line of content: ")
            if text == "stop":
                break
            file.write(text + "\n")


if __name__ == "__main__":
    main()
