def main() -> None:
    file_name = input("Enter name of the file: ")
    txt_file = open(f"{file_name}.txt", "w")
    while True:
        user_input = input("Enter new line of content: ")
        if user_input == "stop":
            break
        txt_file.write(user_input + "\n")

    txt_file.close()


if __name__ == "__main__":
    main()
