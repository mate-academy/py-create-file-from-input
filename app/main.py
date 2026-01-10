def main() -> None:
    filename = input("Enter name of the file: ")
    filename += ".txt"
    with open(filename, "w") as file:
        while True:
            user_input = input("Enter new line of content: ")
            if user_input.lower() == "stop":
                break
            else:
                file.write(user_input + "\n")
                print(f"Enter new line of content: {user_input}")


if __name__ == "__main__":
    main()
