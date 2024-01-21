def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"

    with open(file_name, "w") as file:
        some_text = ""
        while some_text != "stop":
            some_text = input("Enter new line of content: ")
            if some_text != "stop":
                file.write(some_text + "\n")


if __name__ == "__main__":
    main()
