def main() -> None:
    name_file = input("Enter name of the file: ")

    while True:
        content = input("Enter new line of content: ")
        if content == "stop":
            open(f"{name_file}.txt", "a")
            break
        with open(f"{name_file}.txt", "a") as file_:
            (file_.write(f"{content}\n"))


if __name__ == "__main__":
    main()
