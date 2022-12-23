def main() -> None:
    name_file = input("Enter name of the file: ")
    with open(f"{name_file}.txt", "a") as file:
        while True:
            output = input("Enter new line of content: ") + "\n"
            if output != "stop" + "\n":
                file.write(output)
            else:
                break


if __name__ == "__main__":
    main()
