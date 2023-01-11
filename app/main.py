def main() -> None:
    name_file = input("Enter name of the file: ")
    new_file = open(f"{name_file}.txt", "w")
    new_file.close()
    with open(f"{name_file}.txt", "a") as f:
        while True:
            enter_line = input("Enter new line of content: ")
            if enter_line == "stop":
                break
            f.write(f"{enter_line}\n")


if __name__ == "__main__":
    main()
