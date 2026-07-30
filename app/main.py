def main() -> None:
    file_name = input("Enter name of the file: ")

    with open(f"{file_name}.txt", "a") as file:

        while True:
            sent = input("Enter new line of content: ")
            if sent != "stop":
                file.write(sent + "\n")
            else:
                break


if __name__ == "__main__":
    main()
