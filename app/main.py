def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    with open(file_name, "w") as file:
        while True:
            data = input("Enter new line of content: ")

            if data == "stop":
                break

            file.write(data + "\n")


if __name__ == "__main__":
    main()
