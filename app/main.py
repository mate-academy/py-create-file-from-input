def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    with open(file_name, "a") as file:
        user_input = input("Enter new line of content: ")
        while user_input.lower().strip() != "stop":
            file.write(user_input + "\n")
            user_input = input("Enter new line of content: ")
    print(f"File name: '{file_name}'\nFile content: ")
    with open(file_name) as f:
        for line in f.read():
            print(f"# {line}", end="")


if __name__ == "__main__":
    main()
