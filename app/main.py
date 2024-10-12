def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "a") as f:
        pass
    while True:
        user_input = input("Enter new line of content: ")
        if user_input == "stop":
            break
        with open(f"{file_name}.txt", "a") as f:
            f.write(f"{user_input}\n")


if __name__ == "__main__":
    main()
