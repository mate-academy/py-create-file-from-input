def main() -> str:
    file_name = input("Enter name of the file: ")
    if not file_name.endswith(".txt"):
        file_name += ".txt"
    with open(file_name, mode="w") as file:
        while True:

            line = input("Enter new line of content: ")
            if line.lower() == "stop":
                break
            file.write(line + "\n")

    print(f"File '{file_name}' has been created successfully.")


if __name__ == "__main__":
    main()
