def main() -> None:
    file_name = input("Enter name of the file: ")
    text = ""

    while True:
        text = input("Enter new line of content: ")
        if text == "stop":
            with open(f"{file_name}.txt", "a"):
                break
        with open(f"{file_name}.txt", "a") as data:
            data.write(f"{text}\n")


if __name__ == "__main__":
    main()
