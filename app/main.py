class EmptyNameError(ValueError):
    def __str__(self) -> str:
        return "Filename cannot be empty, please provide a name."


def main() -> None:
    try:
        file_name = input("Enter name of the file: ")

        if not file_name.strip():
            raise EmptyNameError()

        file_name += ".txt"

    except EmptyNameError as exe:
        print(exe)
        main()

    except Exception as exe:
        print("An unexpected error occurred:", exe)
        main()

    with open(file_name, "w") as f:
        user_input = ""

        while not user_input == "stop":
            user_input = input("Enter new line of content: ").strip()

            if not user_input == "stop":
                f.write(user_input + "\n")


if __name__ == "__main__":
    main()
