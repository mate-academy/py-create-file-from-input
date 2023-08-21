def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    with open(file_name, "w") as file1:
        while True:
            input_content = input("Enter new line of content: ")
            if input_content == "stop":
                break
            file1.write(input_content + "\n")


if __name__ == "__main__":
    main()
