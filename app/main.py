def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    with open(file_name, "a") as file:
        content = input("Enter new line of content: ")
        while content != "stop":
            file.write(f"{content}\n")
            content = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
