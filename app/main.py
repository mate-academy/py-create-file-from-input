def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(file_name, "a") as file:
        while True:
            content = input("Enter new line of content: ")
            if content != "stop":
                file.write(f"{content}\n")
            else:
                break


if __name__ == "__main__":
    main()
