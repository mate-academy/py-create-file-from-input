def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "a", encoding="utf-8") as file:
        while True:
            data = input("Enter new line of content: ")
            if data == "stop":
                break
            file.write(data + "\n")


if __name__ == "__main__":
    main()
