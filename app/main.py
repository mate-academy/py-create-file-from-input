def main() -> None:
    name = input("Enter name of the file: ") + ".txt"
    with open(name, "w") as f:
        while True:
            line_input = input("Enter new line of content: ")
            if line_input == "stop":
                break
            else:
                f.write(line_input + "\n")


if __name__ == "__main__":
    main()
