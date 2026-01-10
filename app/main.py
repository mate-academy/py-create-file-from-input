def main() -> None:
    with open(input("Enter name of the file: ") + ".txt", "a") as name_file:
        while True:
            enter = input("Enter new line of content: ")
            if enter == "stop":
                break
            name_file.write(f"{enter}\n")


if __name__ == "__main__":
    main()
