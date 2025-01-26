def main() -> None:
    file_name = input("Enter name of the file: ").strip()

    with open(f"{file_name}.txt", "a") as file:
        while True:
            user_input = input("Enter new line of content: ").strip()
            if user_input.lower() == "stop":
                break
            file.write(f"{user_input}\n")


if __name__ == "__main__":
    main()
