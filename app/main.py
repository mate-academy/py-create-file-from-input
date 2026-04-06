def main() -> None:
    file_name = input("Enter name of the file: ")
    file_content = []
    while True:
        user_input = input("Enter new line of content: ")
        if user_input == "stop":
            break
        file_content.append(user_input)
    with open(f"{file_name}.txt", "w") as f:
        f.write("\n".join(file_content))


if __name__ == "__main__":
    main()
