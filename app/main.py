def main() -> None:
    name = input("Enter name of the file: ")
    with open(f"{name}.txt", "a") as text_file:
        while True:
            content = input("Enter new line of content: ")

            if content == "stop":
                break

            text_file.write(content + "\n")


if __name__ == "__main__":
    main()
