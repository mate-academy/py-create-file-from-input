def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "a") as f:
        while True:
            input_text = input("Enter new line of content: ")
            if input_text == "stop":
                break
            f.write(input_text + "\n")
    pass


if __name__ == "__main__":
    main()
