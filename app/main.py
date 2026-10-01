def main() -> None:

    file_name = input("Enter name of the file: ")

    with open(f"{file_name}.txt", "a", encoding="utf-8") as f:

        while True:
            content = input("Enter new line of content: ")

            if content == "stop":
                break
            else:
                f.write(f"{content}\n")


if __name__ == "__main__":
    main()
