def main() -> None:
    name = input("Enter name of the file: ")
    user_input = ""
    res = ""

    while user_input != "stop":
        user_input = input("Enter new line of content: ")
        if user_input != "stop":
            res += user_input + "\n"

    with open(f"{name}.txt", "w") as f:
        f.write(res)


if __name__ == "__main__":
    main()
