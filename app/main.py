def main() -> object:
    name = input("Enter name of the file: ")

    with open(f"{name}.txt", "w") as f:
        new_line = None
        while new_line != "stop":
            new_line = input("Enter new line of content: ")
            if new_line == "stop":
                break
            f.write(f"{new_line}\n")


if __name__ == "__main__":
    main()
