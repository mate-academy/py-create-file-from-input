def main() -> None:
    enter_name = input("Enter name of the file: ")
    with open(f"{enter_name}.txt", "a") as file:
        while True:
            enter_line = input("Enter new line of content: ")
            if enter_line == "stop":
                break
            file.write(f"{enter_line}\n")


if __name__ == "__main__":
    main()
