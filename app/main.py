def main() -> None:
    name = input("Enter name of the file: ")
    with open(f"{name}.txt", "a+") as new_file:
        ls = []
        while True:
            new_line = input("Enter new line of content: ")
            if new_line != "stop":
                ls.append(new_line + "\n")
                continue
            break
        new_file.writelines(ls)


if __name__ == "__main__":
    main()
