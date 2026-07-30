def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "w") as output_file:
        content = ""
        while content != "stop":
            content = input("Enter new line of content: ")
            if content != "stop":
                output_file.write(f"{content}\n")


if __name__ == "__main__":
    main()
