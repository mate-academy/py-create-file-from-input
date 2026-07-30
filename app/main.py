def main() -> None:
    name = input("Enter name of the file: ")
    with open(name + ".txt", "a") as f:
        process = True
        while process:
            next_line = input("Enter new line of content: ")
            if next_line == "stop":
                break
            else:
                f.write(next_line + "\n")


if __name__ == "__main__":
    main()
