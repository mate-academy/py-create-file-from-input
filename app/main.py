def main() -> None:
    # write your code here
    file_name = input("Enter name of the file: ") + ".txt"
    with open(file_name, "w") as file:
        while True:
            line = input("Enter new line of content: ")
            if line == "stop":
                break
            file.write(line + "\n")


if __name__ == "__main__":
    main()
