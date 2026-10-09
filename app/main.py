def main() -> None:
    name = input("Enter name of the file: ")
    file_name = name + ".txt"

    with open(file_name, "w") as firs_file:
        while True:
            string = input("Enter new line of content: ")
            if string == "stop":
                break
            firs_file.write(f"{string}\n")


if __name__ == "__main__":
    main()
