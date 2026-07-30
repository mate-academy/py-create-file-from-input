def main() -> None:
    file_name = input("Enter name of the file: ")
    full_file_name = file_name + ".txt"

    lines = []

    while True:
        user_input = input("Enter new line of content: ")
        if user_input == "stop":
            break
        lines.append(user_input)

    with open(full_file_name, "w") as file_to_create:
        for line in lines:
            file_to_create.write(f"{line}\n")


if __name__ == "__main__":
    main()
