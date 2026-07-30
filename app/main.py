def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "wt") as new_file:
        while True:
            content = input("Enter new line of content: ")
            if content == "stop":
                break
            new_file.write(f"{content}\n")


if __name__ == "__main__":
    main()
