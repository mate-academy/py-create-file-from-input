def main() -> None:
    name_file = input("Enter name of the file: ")
    with open(name_file + ".txt", "a") as file:
        while True:
            new_content = input("Enter new line of content: ")
            if new_content == "stop":
                break
            file.write(new_content + "\n")


if __name__ == "__main__":
    main()
