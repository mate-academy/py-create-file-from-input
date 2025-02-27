def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    with open(file_name, "w") as file:
        while (content := input("Enter new line of content: ")) != "stop":
            file.write(content + "\n")


if __name__ == "__main__":
    main()
