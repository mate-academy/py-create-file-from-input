def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    with open(file_name, "a") as file:
        flag = True
        while flag:
            text = input("Enter new line of content: ")
            if text == "stop":
                flag = False
            else:
                text += "\n"
                file.write(text)


if __name__ == "__main__":
    main()
