def main() -> None:
    filename = input("Enter name of the file: ") + ".txt"
    cont = []
    new_line = input("Enter new line of content: ")
    while new_line != "stop":
        cont.append(new_line)
        new_line = input("Enter new line of content: ")

    to_add = "\n".join(cont)
    with open(filename, "w") as f:
        f.write(to_add)


if __name__ == "__main__":
    main()
