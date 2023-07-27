def main() -> None:
    print("Enter name of the file: ", end="")
    file_name = input()
    with open(file_name + ".txt", "w") as file:
        line = ""
        while line != "stop":
            print("Enter new line of content: ", end="")
            line = input()
            file.write(line + "\n")


if __name__ == "__main__":
    main()