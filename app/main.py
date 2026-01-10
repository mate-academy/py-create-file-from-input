def main() -> None:
    file_name = input("Enter name of the file: ")
    data = ""
    while True:
        user_input = input("Enter new line of content: ")
        if user_input == "stop":
            break
        data += user_input + "\n"

    with open(file_name + ".txt", "w") as f:
        f.write(data)


if __name__ == "__main__":
    main()
