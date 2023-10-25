def main() -> None:
    name_of_file = input("Enter name of the file: ")
    new_file = open(f"{name_of_file}.txt", "a")
    while True:
        content = input("Enter new line of content: ")
        if content == "stop":
            break
        new_file.write(f"{content}\n")
    new_file.close()


if __name__ == "__main__":
    main()
