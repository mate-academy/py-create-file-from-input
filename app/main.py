def main() -> None:
    name_of_file = input("Enter name of the file: ")
    content_file = input("Enter new line of content: ")
    with open(f"{name_of_file}.txt", "w") as file:
        while True:
            if content_file != "stop":
                file.write(f"{content_file}\n")
                content_file = input("Enter new line of content: ")
            else:
                break


if __name__ == "__main__":
    main()
