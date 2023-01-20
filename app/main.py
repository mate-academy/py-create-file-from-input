def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "a+") as f:
        while True:
            content = input("Enter new line of content: ")
            if content == "stop":
                break
            f.write(f"{content}\n")


if __name__ == "__main__":
    main()
