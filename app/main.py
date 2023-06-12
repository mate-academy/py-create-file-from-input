def main() -> None:
    title = input("Enter name of the file: ")
    while True:
        content = input("Enter new line of content: ")
        with open(title + ".txt", "a") as file:
            if content == "stop":
                break
            file.write(f"{content}\n")


if __name__ == "__main__":
    main()
