def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(file_name + ".txt", "a") as file:
        content = ""
        while content != "stop":
            content = input("Enter new line of content: ")
            if content != "stop":
                file.write(f"{content}\n")


if __name__ == "__main__":
    main()
