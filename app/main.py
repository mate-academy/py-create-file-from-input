def main() -> None:
    file_name = input("Enter name of the file: ")

    with open(file_name + ".txt", "w") as new_request:
        while True:
            input_string = input("Enter new line of content: ")
            if input_string == "stop":
                break
            else:
                new_request.write(input_string + "\n")


if __name__ == "__main__":
    main()
