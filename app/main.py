def main() -> None:
    name = input("Enter name of the file: ")
    with open(f"{name}.txt", "a") as new_file:
        while True:
            line = input("Enter new line of content: ")
            if line == "stop":
                break
            new_file.write(f"{line}\n")


if __name__ == "__main__":
    main()
