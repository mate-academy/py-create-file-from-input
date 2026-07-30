def main() -> None:
    name = input("Enter name of the file: ")
    filename = name + ".txt"
    with open(filename, "a") as fp:
        new_str = ""
        while True:
            new_str = input("Enter new line of content: ")
            if new_str == "stop":
                break
            fp.write(new_str + "\n")


if __name__ == "__main__":
    main()
