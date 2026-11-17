def main() -> None:
    file_name = input("Enter name of the file: ")
    file_data = input("Enter new line of content: ")
    with open(f"{file_name}.txt", "w") as file:
        while file_data != "stop":
            file.write(file_data + "\n")
            file_data = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
