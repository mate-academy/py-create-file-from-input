def main() -> None:
    user_filename = input("Enter name of the file: ")
    with open(f"{user_filename}.txt", "w") as file:
        while True:
            data = input("Enter new line of content: ")
            if data.lower() == "stop":
                break
            file.write(data + "\n")


if __name__ == "__main__":
    main()
