def main() -> None:
    message = ""
    input_name = input("Enter name of the file: ")

    if input_name:
        while True:
            inp_message = input("Enter new line of content: ")

            if inp_message == "stop":
                break
            message += f"{inp_message}\n"

    file_name = f"{input_name}.txt"
    file_discriptor = open(file_name, "w")
    file_discriptor.write(message)
    file_discriptor.close()


if __name__ == "__main__":
    main()
