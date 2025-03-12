def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    with open(file_name, "a") as user_data:
        while True:
            input_text = input("Enter new line of content: ")
            if input_text == "stop":
                break
            user_data.write(input_text + "\n")


if __name__ == "__main__":
    main()
