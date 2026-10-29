def main() -> None:

    file_name = input("Enter name of the file: ")
    data = ""
    with open(file_name + ".txt", "a") as file:
        while data != "stop":
            data = input("Enter new line of content: ")
            if data != "stop":
                file.write(data + "\n")


if __name__ == "__main__":
    main()
