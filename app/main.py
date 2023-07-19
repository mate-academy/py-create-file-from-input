def main() -> None:
    name = input("Enter name of the file: ")
    file_name = name + ".txt"
    new_file = open(file_name, "w")
    new_file.close()
    with open(file_name, "a") as file:
        while True:
            line = input("Enter new line of content: ")
            if line != "stop":
                file.write(f"{line}\n")
                continue
            break


if __name__ == "__main__":
    main()
