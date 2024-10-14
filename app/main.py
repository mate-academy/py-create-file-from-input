def main() -> None:
    name = f'{input("Enter name of the file: ")}.txt'
    with open(name, "w") as f:
        while True:
            user_input = input("Enter new line of content: ")
            if user_input.lower() == "stop":
                break
            f.write(f"{user_input}\n")


if __name__ == "__main__":
    main()
