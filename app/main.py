def main() -> None:
    with open(input("Enter name of the file: ") + ".txt", mode="w") as file:
        while True:
            content = input("Enter new line of content: ")
            if content.lower() == "stop":
                break
            else:
                file.writelines(content + "\n")


if __name__ == "__main__":
    main()
