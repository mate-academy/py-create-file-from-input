def main() -> None:
    file_name = input("Enter name of the file: ")
    if file_name == "":
        return

    txt_file_path = f"{file_name}.txt"

    with open(txt_file_path, "a") as file:
        while True:
            content_for_file = input("Enter new line of content: ")
            if content_for_file.lower() == "stop":
                return

            file.write(f"{content_for_file}\n")


if __name__ == "__main__":
    main()
