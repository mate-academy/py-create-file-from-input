def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    with open(file_name, "w") as file:
        while True:
            enter_content = input("Enter new line of content: ")
            if enter_content.lower() == "stop":
                break
            file.write(enter_content + "\n")


if __name__ == "__main__":
    main()
