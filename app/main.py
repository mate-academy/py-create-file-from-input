def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    with open(file_name, "a") as f:
        while True:
            file_content = input("Enter new line of content: ")
            if file_content != "stop":
                f.write(file_content + "\n")
            else:
                break


if __name__ == "__main__":
    main()
