def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(file_name + ".txt", "w") as file1:
        text = ""
        while text != "stop":
            text = input("Enter new line of content: ")
            if text != "stop":
                file1.write(text + "\n")


if __name__ == "__main__":
    main()
