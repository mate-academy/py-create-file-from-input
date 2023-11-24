def main() -> None:
    name = input("Enter name of the file: ")
    flag = True
    needed_file = open(name + ".txt", "a")

    while flag:
        new_line = input("Enter new line of content: ")

        if new_line == "stop":
            flag = False
            break

        needed_file.write(new_line + "\n")


if __name__ == "__main__":
    main()
