def main() -> None:
    name = input("Enter name of the file: ")
    name += ".txt"
    with (open(name, "a") as f):
        while True:
            file_content = input("Enter new line of content: ")
            if file_content == "stop":
                break
            f.write(file_content + "\n")


if __name__ == "__main__":
    main()
