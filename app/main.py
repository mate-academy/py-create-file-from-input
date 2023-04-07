def main() -> None:
    user_text1 = input("Enter name of the file: ")
    new_file = open(user_text1 + ".txt", "a")
    while True:
        user_text2 = input("Enter new line of content: ")
        if user_text2 == "stop":
            break
        new_file.write(user_text2 + "\n")


if __name__ == "__main__":
    main()
