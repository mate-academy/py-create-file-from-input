def main() -> None:
    name = input("Enter name of the file: ")
    file_name = open(name + ".txt", "w")
    text = input("Enter new line of content: ")
    while text != "stop":
        file_name.write(text + "\n")
        text = input("Enter new line of content: ")
    file_name.close()


if __name__ == "__main__":
    main()
