def main() -> None:
    file_name = input("Enter name of the file: ")
    file_name = file_name + ".txt"
    with open(file_name, "a") as file:
        while True:
            insert_data = input("Enter new line of content: ")
            if insert_data.lower() == "stop":
                break
            file.write(f"{insert_data}\n")


if __name__ == "__main__":
    main()
