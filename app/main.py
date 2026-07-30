def main() -> None:
    name = input("Enter name of the file: ")

    with open(f"{name}.txt", "w") as file:
        while True:
            content_line = input("Enter new line of content: ")
            if content_line == "stop":
                break
            file.write(f"{content_line}\n")


if __name__ == "__main__":
    main()
