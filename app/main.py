def main() -> None:
    file_name = input("Enter name of the file: ")
    file_content = file_name + ".txt"
    with open(file_content, "w") as f:
        while True:
            content = input("Enter new line of content: ")
            if content.lower() == "stop":
                break
            f.write(content + "\n")


if __name__ == "__main__":
    main()
