def main() -> None:

    name_of_file = input("Enter name of the file:")
    with open(name_of_file, "w") as current_file:
        line = current_file.write(input("Enter new line of content:"))
        while True:
            line
            if line == "stop":
                break


if __name__ == "__main__":
    main()
