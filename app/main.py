def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"

    open(file_name, "w")

    with open(file_name, "a") as f:
        while True:
            content = input("Enter new line of content: ")

            if content == "stop":
                break

            f.write(content + "\n")


if __name__ == "__main__":
    main()
