def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(file_name + ".txt", "a") as file:
        while True:
            input_content = input("Enter new line of content: ")
            if "stop" in input_content.lower():
                break
            file.write(input_content + "\n")


if __name__ == "__main__":
    main()
