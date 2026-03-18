def main() -> None:
    users_input_name = input("Enter name of the file: ")
    file_name = f"{users_input_name}.txt"
    with open(file_name, "w") as file:
        while True:
            line = input("Enter new line of content: ")
            if line == "stop":
                break
            file.write(line + "\n")


if __name__ == "__main__":
    main()
