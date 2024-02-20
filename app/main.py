def main() -> None:
    file_name = input("Enter name of the file: ")
    full_path = f"{file_name}.txt"
    while 1:
        with open(full_path, "a") as f:
            content = input("Enter new line of content: ")
            if content == "stop":
                break
            f.write(content + "\n")


if __name__ == "__main__":
    main()
