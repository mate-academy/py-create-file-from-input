def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    with open(file_name, mode="w", ) as output_file:
        while True:
            content = input("Enter new line of content: ")
            if content == "stop":
                break

            output_file.write(f"{content}\n")


if __name__ == "__main__":
    main()
