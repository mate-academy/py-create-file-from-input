def main() -> None:
    name_of_file = input("Enter name of the file: ")
    with open(f"{name_of_file}.txt", "w") as file:

        while True:
            print_data = input("Enter new line of content: ")
            if print_data == "stop":
                break
            file.write(print_data + "\n")


if __name__ == "__main__":
    main()
