def main() -> None:
    name_of_file = input("Enter name of the file: ")
    res = f"{name_of_file}.txt"
    with open(res, "w") as file:
        while True:
            new_line = input("Enter new line of content: ")
            if new_line.lower() == "stop":
                break
            file.write(new_line + "\n")


if __name__ == "__main__":
    main()
