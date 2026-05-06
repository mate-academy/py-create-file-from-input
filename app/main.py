def main() -> None:
    with open(input("Enter name of the file: ") + ".txt", "a") as file:
        while True:
            text_to_write = input("Enter new line of content: ")
            if text_to_write == "stop":
                break
            file.write(text_to_write + "\n")


if __name__ == "__main__":
    main()
