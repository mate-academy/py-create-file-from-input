def main() -> None:
    with open(input("Enter name of the file: ") + ".txt", "a") as file:
        while True:
            content = input("Enter new line of content: ") + "\n"
            if content == "stop\n":
                break
            file.write(content)


if __name__ == "__main__":
    main()
