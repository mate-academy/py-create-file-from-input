def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "a") as file:
        flag = True
        while flag:
            line = input("Enter new line of content: ")
            if line == "stop":
                flag = False
                break
            file.write(line + "\n")


if __name__ == "__main__":
    main()
