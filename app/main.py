def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "w") as file:
        while True:
            current_text = input("Enter new line of content: ")
            if current_text == "stop":
                break
            else:
                file.write(f"{current_text}\n")


if __name__ == "__main__":
    main()
