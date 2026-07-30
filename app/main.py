def main() -> None:
    name = input("Enter name of the file: ")
    file_name = open(f"{name}.txt", "a")
    while True:
        text = input("Enter new line of content: ")
        if text == "stop":
            break
        file_name.write(f"{text}\n")


if __name__ == "__main__":
    main()
