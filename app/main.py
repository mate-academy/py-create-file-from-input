def main() -> None:
    name = input("Enter name of the file: ")
    name = name + ".txt"
    ls = []
    while True:
        inn = input("Enter new line of content: ")
        if inn != "stop":
            ls.append(inn)
        else:
            break
    with open(name, "w") as new_f:
        for line in ls:
            new_f.write(line + "\n")


if __name__ == "__main__":
    main()
