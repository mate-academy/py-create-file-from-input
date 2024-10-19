def main() -> None:
    name = input("Enter name of the file: ")
    text_file = open(f"{name}.txt", "a")
    while True:
        text = input("Enter new line of content: ")
        if text == "stop":
            break
        text_file.write(f"{text}\n")


if __name__ == "__main__":
    main()
