def main() -> None:
    file_name = input("Enter name of the file: ")
    with open(f"{file_name}.txt", "a") as file_name:
        while True:
            output = input("Enter new line of content: ") + "\n"
            if output != "stop" + "\n":
                file_name.write(output)
            else:
                break


if __name__ == "__main__":
    main()
