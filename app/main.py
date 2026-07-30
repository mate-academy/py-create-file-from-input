def main() -> None:
    filename = input("Enter name of the file: ")
    with open(f"{filename}.txt", "a") as f:
        user_input = ""
        while True:
            user_input = input("Enter new line of content: ")
            if user_input == "stop":
                break
            f.write(user_input + "\n")


if __name__ == "__main__":
    main()
