def main() -> None:
    input_user = input("Enter name of the file: ")
    with open(input_user + ".txt", "w") as file:
        while input_user != "stop\n":
            input_user = f"{input("Enter new line of content: ")}\n"
            print(input_user)
            file.write(input_user if input_user != "stop\n" else "")


if __name__ == "__main__":
    main()
