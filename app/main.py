def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    with open(file_name, "w") as file_to_write:
        while 1:
            content = input("Enter new line of content: ")
            if content == "stop":
                break
            file_to_write.write(content + "\n")


if __name__ == "__main__":
    main()
