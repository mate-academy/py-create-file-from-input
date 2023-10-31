def main() -> None:
    name = input("Enter name of the file: ")

    file_name = f"{name}.txt"

    with open(file_name, "w") as file:
        while True:
            new_line = input("Enter new line of content: ")
            if new_line == "stop":
                break
            file.write(f"{new_line}\n")


if __name__ == "__main__":
    main()
