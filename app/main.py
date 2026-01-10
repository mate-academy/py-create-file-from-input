def main() -> None:
    file_name = input("Enter name of the file: ")

    with open(f"{file_name}.txt", "w") as file:
        while True:
            new_input = input("Enter new line of content: ")
            if new_input != "stop":
                file.write(new_input + "\n")
            else:
                break


if __name__ == "__main__":
    main()
