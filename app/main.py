def main() -> None:
    # write your code here
    with open(f"""{input("Enter name of the file: ")}.txt""", "a") as file:
        while True:
            user_input = input("Enter new line of content: ")
            if user_input == "stop":
                break
            file.write(f"{user_input}\n")


if __name__ == "__main__":
    main()
