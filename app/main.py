def main() -> None:
    name = input("Enter name of the file: ")
    line_input = ""
    with open(f"{name}.txt", "w+") as f:
        f.close()
    while line_input != "stop":
        line_input = input("Enter new line of content: ")
        if line_input != "stop":
            with open(f"{name}.txt", "a+") as f:
                f.write(f"{line_input}\n")
        f.close()


if __name__ == "__main__":
    main()
