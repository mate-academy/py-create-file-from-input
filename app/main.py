def main() -> None:
    name_of_file = input("Enter name of the file: ")
    name_of_file = name_of_file + ".txt"
    with open(name_of_file, "w") as file:
        while True:
            line = input("Enter new line of content: ")
            if line == "stop":
                break
            file.write(f"{line}\n")


if __name__ == "__main__":
    main()
