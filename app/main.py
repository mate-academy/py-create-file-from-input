def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name = file_name + ".txt"
    file_result = open(file_name, "w")
    while True:
        user_input = input("Enter new line of content: ")
        if user_input.strip().lower() == "stop":
            file_result.close()
            break
        file_result.write(user_input)
        file_result.write("\n")
    file_result.close()


if __name__ == "__main__":
    main()
