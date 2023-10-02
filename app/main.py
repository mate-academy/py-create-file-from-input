def main() -> None:
    name = input("Enter name of the file: ")
    with open(f"{str(name)}.txt", "w") as file:
        while True:
            content_input = input("Enter new line of content: ")
            if content_input == "stop":
                break
            file.write(content_input + "\n")


if __name__ == "__main__":
    main()
