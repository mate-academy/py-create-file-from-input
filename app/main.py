def main() -> None:
    filename = input("Enter name of the file: ")
    open(f"{filename}.txt", "x")
    while True:
        new_line = input("Enter new line of content: ")
        if new_line == "stop":
            break
        else:
            with open(f"{filename}.txt", "a") as f:
                f.write(new_line + "\n")


if __name__ == "__main__":
    main()
