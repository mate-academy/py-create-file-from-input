def main() -> None:
    name = input("Enter name of the file: ")
    name += ".txt"
    with open(name, "tw") as f:
        while True:
            input_str = input("Enter new line of content: ")
            if input_str == "stop":
                break
            input_str += "\n"
            f.write(input_str)


if __name__ == "__main__":
    main()
