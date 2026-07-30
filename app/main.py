def main() -> None:
    f_name = input("Enter name of the file: ") + ".txt"
    f_contest = ""

    while True:
        new_line = input("Enter new line of content: ")
        if new_line.lower() == "stop":
            break
        else:
            f_contest += new_line + "\n"

    with open(f_name, "w") as f:
        f.write(f_contest)


if __name__ == "__main__":
    main()
