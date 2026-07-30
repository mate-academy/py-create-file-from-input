def main() -> None:
    name = input("Enter name of the file: ")
    with open(f"{name}.txt", "w") as f:
        while True:
            user_text = input("Enter new line of content: ")
            if user_text == "stop":
                break
            f.write(user_text + "\n")


if __name__ == "__main__":
    main()
