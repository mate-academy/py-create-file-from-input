def main() -> None:
    extension = ".txt"

    file_name = input("Enter name of the file: ") + extension

    lines = []

    print("Enter file content('stop' to finish):")
    while True:
        user_input = input("Enter new line of content: ")
        if user_input == "stop":
            break
        lines.append(user_input)

    with open(file_name, "w") as file:
        for line in lines:
            file.write(f"{line}\n")


if __name__ == "__main__":
    main()
