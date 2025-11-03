def main() -> None:
    file_name = input("Enter name of the file: ")

    with open(f"{file_name}.txt", "w") as f:

        while True:
            content_line = input("Enter new line of content: ")
            if content_line == "stop":
                break
            f.write(content_line + "\n")


if __name__ == "__main__":
    main()
