def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name += ".txt"
    file_text = open(file_name, "w")
    with open(file_name, "a") as file_text:
        while True:
            content = input("Enter new line of content: ")
            if content == "stop":
                break
            else:
                file_text.write(content)
                file_text.write("\n")


if __name__ == "__main__":
    main()
