def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(file_name + ".txt", "w") as file:
        response = None
        while response != "stop":
            response = input("Enter new line of content: ")
            if response != "stop":
                file.write(response + "\n")


if __name__ == "__main__":
    main()
