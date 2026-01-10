def main() -> None:
    filename = input("Enter name of the file: ") + ".txt"
    while True:
        with open(filename, "a") as file:
            file_input = input("Enter new line of content: ")
            if file_input != "stop":
                file.write(file_input + "\n")
            else:
                break
    file.close()
    print(f'File name: "{filename}\nFile content: "')
    with open(filename, "r") as file:
        for line in file:
            print(line, end="")


if __name__ == "__main__":
    main()
