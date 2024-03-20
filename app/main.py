def main() -> None:
    file_name = input("Enter name of the file: ")

    line = input("Enter new line of content: ")

    with open(f"{file_name}.txt", "w") as f:
        while line != "stop":
            f.write(f"{line}\n")
            line = input("Enter new line of content: ")


if __name__ == "__main__" :
    main()
