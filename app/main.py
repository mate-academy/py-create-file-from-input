def main() -> None:
    file_name = input("Enter name of the file: ")
    name = file_name + ".txt"

    with open(name, "w") as file:
        while True:
            first_str = input("Enter new line of content: ")
            if first_str == "stop":
                break
            else:
                file.write(first_str + "\n")


if __name__ == "__main__":
    main()
