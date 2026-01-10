def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name += ".txt"

    with open(file_name, "w") as f:
        while True:
            user_input = input("Enter new line of content: ")
            if user_input.lower() == "stop":
                break
            f.write(user_input + "\n")
    print(f'File name: "{file_name}"')
    print("File content:")
    with open(file_name, "r") as f:
        for line in f:
            print(line, end="")


if __name__ == "__main__":
    main()
