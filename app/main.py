def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    with open(file_name, "w") as file:
        content = ""
        while True:
            text = input("Enter new line of content: ")
            if text == "stop":
                break
            content += (text + "\n")
        file.write(content)


if __name__ == "__main__":
    main()
