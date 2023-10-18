def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    with open(file_name, "w") as f:
        while True:
            user_input = input("Enter new line of content: ")
            if user_input == "stop":
                break
            f.write(user_input + "\n")


if __name__ == "__main__":
    main()
