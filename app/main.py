def main() -> None:
    file_name = input("Enter name of the file: ")
    while True:
        with open(f"{file_name}.txt", "a") as f:
            new_content = input("Enter new line of content: ")
            if new_content == "stop":
                break
            f.write(new_content + "\n")


if __name__ == "__main__":
    main()
