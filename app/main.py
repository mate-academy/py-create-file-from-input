def main() -> None:
    name = input("Enter name of the file: ")
    new = []
    while True:
        string = input("Enter new line of content: ")
        if string == "stop":
            break
        new.append(string)
    na_name = name + ".txt"
    with open(na_name, "w") as f:
        f.write("\n".join(new))


if __name__ == "__main__":
    main()
