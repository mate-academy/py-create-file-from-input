def main() -> None:
    name = input("Enter name of the file: ")
    with open(f"{name}.txt", "w") as new_file:
        while True:
            new_line = input("Enter new line of content: ")
            if new_line == "stop":
                break
            new_file.write(f"{new_line}\n")


if __name__ == "__main__":
    main()
