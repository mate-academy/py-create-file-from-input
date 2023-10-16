def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "w+") as file:
        text = input("Enter new line of content: ")
        while text != "stop":
            file.write(text + "\n")
            text = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
