def main() -> None:
    with open(input("Enter name of the file: ") + ".txt", "a") as f:
        while True:
            new_line = input("Enter new line of content: ") + "\n"
            if new_line == "stop\n":
                break
            f.write(new_line)


if __name__ == "__main__":
    main()
