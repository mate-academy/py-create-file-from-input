def main() -> None:
    file_name = str(input("Enter name of the file: "))
    with open(f"{file_name}.txt", "w") as file:
        while True:
            text = str(input("Enter new line of content: "))
            if text == "stop":
                break
            file.write(f"{text}\n")


if __name__ == "__main__":
    main()
