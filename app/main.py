def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "w+") as f:
        while True:
            inp_line = input("Enter new line of content: ")
            if inp_line == "stop":
                break
            else:
                f.write(f"{inp_line}\n")


if __name__ == "__main__":
    main()
