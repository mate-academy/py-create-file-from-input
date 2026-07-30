def main() -> None:
    file_name = input("Enter name of the file: ")

    with open(f"{file_name}.txt", "w") as file_pointer:
        while True:
            file_content = input("Enter new line of content: ")
            if file_content == "stop":
                return

            file_pointer.write(f"{file_content}\n")


if __name__ == "__main__":
    main()
