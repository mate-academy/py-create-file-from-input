def main() -> None:
    name_of_file = input("Enter name of the file: ")

    with open(name_of_file + ".txt", "a") as f:
        while True:
            content = input("Enter new line of content: ")
            if content == "stop":
                return
            f.write(content + "\n")


if __name__ == "__main__":
    main()
