def main() -> None:
    file_name = (f"{input("Enter name of the file: ")}.txt")

    line = input("Enter new line of content: ")

    with open(file_name, "w") as f:
        while line != "stop":
            f.write(f"{line}\n")
            line = input("Enter new line of content: ")


if __name__ == "__main__" :
    main()
