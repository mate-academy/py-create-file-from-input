def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "w") as file:
        while True:
            user_text = input("Enter new line of content: ")
            if user_text == "stop":
                break
            file.write(f"{user_text}\n")


if __name__ == "__main__":
    main()
