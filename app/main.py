def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "a") as file:
        while True:
            line_to_write = input("Enter new line of content: ") + "\n"
            if line_to_write != "stop" + "\n":
                file.write(line_to_write)
            else:
                break


if __name__ == "__main__":
    main()
