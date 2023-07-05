def main() -> None:
    name_of_file = str(input("Enter name of the file: "))
    st_line = ""
    with open(f"{name_of_file}.txt", "w") as filik:
        while True:
            line = str(input("Enter new line of content: "))
            if line != "stop":
                st_line += line + "\n"
            else:
                filik.write(st_line)
                break


if __name__ == "__main__":
    main()
