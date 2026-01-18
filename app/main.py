def main() -> None:
    fille_name = input("Enter name of the file: ")
    content = ""
    while True:
        current_input = input("Enter new line of content: ")
        if current_input == "stop":
            break
        content = content + current_input + "\n"
    with open(f"{fille_name}.txt", "x") as file:
        file.write(content)


if __name__ == "__main__":
    main()
