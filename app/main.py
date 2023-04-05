def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name += ".txt"
    with open(file_name, "w") as f:
        line = ""
        while line != "stop":
            line = input("Enter new line of content: ")
            if line != "stop":
                f.write(line + "\n")


if __name__ == "__main__":
    main()
