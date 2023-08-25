def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "w") as content_file:
        while (content := input("Enter new line of content: ")) != "stop":
            content_file.write(f"{content}\n")


if __name__ == "__main__":
    main()
