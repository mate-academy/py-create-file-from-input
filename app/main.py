def main() -> None:
    with open(input("Enter name of the file: ") + ".txt", "w") as name_file:
        while True:
            data_add = input("Enter new line of content: ")
            if data_add == "stop":
                break
            name_file.write(f"{data_add}\n")


if __name__ == "__main__":
    main()
