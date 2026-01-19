def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"

    with open(file_name, "a") as file_obj:
        while True:
            line = input("Enter new line of content: ")
            if line == "stop":
                break
            file_obj.write(line + "\n")


if __name__ == "__main__":
    main()
