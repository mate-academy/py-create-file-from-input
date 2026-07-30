def main() -> None:
    name_of_the_file = input("Enter name of the file: ")
    with open(name_of_the_file + ".txt", "a") as file:
        while True:
            text = input("Enter new line of content: ")
            if text == "stop":
                break
            else:
                file.write(text + "\n")


if __name__ == "__main__":
    main()
