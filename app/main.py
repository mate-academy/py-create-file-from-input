def main() -> None:
    name = input("Enter name of the file: ")
    filename = name + ".txt"

    try:
        with open(filename, "w") as file:
            while True:
                content = input("Enter new line of content: ")
                if content.lower() == "stop":
                    break
                file.write(content + "\n")
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        print(
            f"File '{filename}' has been created successfully "
            f"with the following content:"
        )
        with open(filename, "r") as file:
            print(file.read())


if __name__ == "__main__":
    main()
