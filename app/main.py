def main() -> None:
    file_name = None
    flag = True
    while flag:
        if file_name is None:
            file_name = input("Enter name of the file: ")
        user_input = input("Enter new line of content: ")
        new_file = open(f"{file_name}.txt", "a")
        if user_input == "stop":
            flag = False
            new_file.close()
        else:
            new_file.write(user_input + "\n")
    print(f"File name: {file_name}")


if __name__ == "__main__":
    main()
