def main() -> None:
    user = input("Enter name of the file: ")
    with open(f"{user}.txt", "a") as file:
        while True:
            user_text = input("Enter new line of content: ")
            if user_text == "stop":
                break
            file.write(f"{user_text}\n")


if __name__ == "__main__":
    main()
