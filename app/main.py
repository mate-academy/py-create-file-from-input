def main() -> None:
    name = input("Enter name of the file: ")
    if not name:
        return
    with open(f"{name}.txt", "w") as file:
        while True:
            content = input("Enter new line of content: ")
            if content == "stop":
                return
            file.write(f"{content}\n")


if __name__ == "__main__":
    main()
