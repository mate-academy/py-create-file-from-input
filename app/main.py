def main() -> None:
    file_name = input("Enter name of the file: ")
    full_file_name = f"{file_name}.txt"
    with open(full_file_name, "w") as f:
        while True:
            stop_input = input("Enter new line of content: ")
            if stop_input != "stop":
                writer = f"{stop_input}\n"
                f.write(writer)
            else:
                break


if __name__ == "__main__":
    main()
