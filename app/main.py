def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    content = None
    with open(file_name, "w") as file:
        while content != "stop":
            content = input("Enter new line of content: ")
            if content == "stop":
                break
            elif content != "stop" and content is not None:
                file.write(content + "\n")
            else:
                pass


if __name__ == "__main__":
    main()
