def main() -> None:
    input_name = input("Enter name of the file: ") + ".txt"

    with open(input_name, "a") as file:
        while True:
            input_content = input("Enter new line of content: ")
            if input_content == "stop":
                break
            file.write(input_content + "\n")

    file.close()


if __name__ == "__main__":
    main()
