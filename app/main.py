def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    with open(file_name, "w") as file:
        new_text = ""
        while True:
            text = input("Enter new line of content: ")
            if text == "stop":
                break
            new_text += (text + "\n")
        file.write(new_text)


if __name__ == "__main__":
    main()
