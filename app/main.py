def main() -> None:
    filename = input("Enter name of the file: ")
    with open(f"{filename}.txt", "w") as f:
        new_enter_string = input("Enter new line of content: ")
        while new_enter_string != "stop":
            f.write(f"{new_enter_string}\n")
            new_enter_string = input("Enter new line of content: ")


if __name__ == "__main__":
    main()
