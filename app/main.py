def main() -> object:
    with open(input("Enter name of the file: ") + ".txt", "a") as text:
        while True:
            new_line = input("Enter new line of content: ")
            if new_line == "stop":
                break
            text.write(f"{new_line}\n")


if __name__ == "__main__":
    main()
