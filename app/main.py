def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    content = ""
    with open(file_name, "w") as file_in:
        while content != "stop":
            content = input("Enter new line of content: ")
            if content != "stop":
                file_in.write(content + "\n")


if __name__ == "__main__":
    main()
