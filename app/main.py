def main() -> None:
    name_of_file = input("Enter name of the file: ")
    with open(name_of_file + ".txt", "w") as opened_file:
        while True:
            line_in_file = input("Enter new line of content: ")
            if "stop" in line_in_file:
                opened_file.close()
                break
            opened_file.write(line_in_file + "\n")


if __name__ == "__main__":
    main()
