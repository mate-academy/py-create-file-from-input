def main() -> None:
    name = input("Enter name of the file: ")
    line = input("Enter new line of content: ")
    file_txt = open(f"{name}.txt", "w")
    while line != "stop":
        file_txt.write(line + "\n")
        line = input("Enter new line of content: ")
    file_txt.close()


if __name__ == "__main__":
    main()
