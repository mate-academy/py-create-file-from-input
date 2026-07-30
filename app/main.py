def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(file_name + ".txt", "a") as f:
        while True:
            content = input("Enter new line of content: ")
            if content == "stop":
                break
            print(content, file=f)


if __name__ == "__main__":
    main()
