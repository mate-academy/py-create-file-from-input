def main() -> None:
    name_file = input("Enter name of the file: ")
    with open(f"{name_file}.txt", "a") as f:
        while True:
            input_text = input("Enter new line of content: ")
            if input_text == "stop":
                break
            f.write(input_text + "\n")


if __name__ == "__main__":
    main()
