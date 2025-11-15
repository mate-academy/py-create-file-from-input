def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(file_name + ".txt", "a") as file:
        while True:
            print("To finish type in 'stop'")
            line = input("Enter new line of content: ")
            if line == "stop":
                break
            file.write(line + "\n")


if __name__ == "__main__":
    main()
