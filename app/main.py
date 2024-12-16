def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"

    with open(file_name, "w") as file:
        print("Enter new line of content. For ending enter 'stop'.")
        while True:
            content = input("Enter new line of content: ")

            if content.lower() == "stop":
                break

            file.write(content + "\n")

    print("File created successfully.")


if __name__ == "__main__":
    main()
