def main() -> None:

    file_name = input("Enter name of the file: ") + ".txt"

    while True:
        content = input("Enter new line of content: ")
        with open(file_name, "a") as f:
            if content == "stop":
                break
            f.write(f"{content}\n")


if __name__ == "__main__":
    main()
