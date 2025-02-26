def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    information = []
    while True:
        print("To finish, enter 'stop'.")
        info = input("Enter new line of content: ")git
        if info.lower() == "stop":
            break
        information.append(info)

    with open(file_name, "w") as file:
        for line in information:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
