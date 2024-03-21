def main() -> None:
    name = input("Enter name of the file: ")
    file_name = f"{name}.txt"
    with open(file_name, "a") as new_file:
        while True:
            line = input("Enter new line of content: ")
            if line != "stop":
                new_file.write(f"{line}\n")
            else:
                break


if __name__ == "__main__":
    main()
