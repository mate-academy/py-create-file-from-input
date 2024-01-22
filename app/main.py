def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    with open(file_name, "w") as f:
        content = ""
        while content != "stop":
            content = input("Enter new line of content: ")
            if content != "stop":
                f.write(content + "\n")


if __name__ == "__main__":
    main()
