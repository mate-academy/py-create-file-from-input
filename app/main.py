def main() -> None:
    file_name = input("Enter name of the file: ")
    content_to_write = None
    with open(f"{file_name}.txt", "w") as f:
        while content_to_write != "stop":
            content_to_write = input("Enter new line of content: ")
            if content_to_write != "stop":
                f.write(f"{content_to_write}\n")


if __name__ == "__main__":
    main()
