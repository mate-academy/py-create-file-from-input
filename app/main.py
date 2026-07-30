def main() -> None:
    name = input("Enter name of the file: ")
    file_name = f"{name}.txt"
    with open(file_name, "w"):
        pass
    while True:
        user_input = input("Enter new line of content: ")
        if user_input.lower() == "stop":
            break
        if user_input.strip() == "":
            continue
        else:
            with open(file_name, "a") as f:
                f.write(f"{user_input}\n")


if __name__ == "__main__":
    main()
