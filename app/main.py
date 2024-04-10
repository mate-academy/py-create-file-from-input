def main() -> None:
    title = input("Enter name of the file: ")
    content = ""
    with open(f"{title}.txt", "a") as file:
        while content.lower().strip() != "stop":
            content = input("Enter new line of content: ")
            if content != "stop":
                file.write(f"{content}\n")


if __name__ == "__main__":
    main()
